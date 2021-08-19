class Solution:
    def isvalid(self, C):
        if len(C) > 2:
            return False
        if len(C) == 1:
            a = min(C)
            if a == 1 or C[a] == 1:
                # EXPLANATION:
                #   a==1   : All lengths are unitary like A=[1,2,3,4,...], so poping anything is fine
                #   C[a]==1: We have a unique length occurence like A=[4,4,4,4,...], so poping anything is fine too
                return True
            # EXPLANATION:
            #     For all other cases of len(C)==1, we'd end with a mistmatch like [1,1,2,2,2], or [1,1,1], so we need to \"return False\" right away
            return False
        #
        # --------- len(D)==2 --------------
        #
        a, b = sorted(C)
        # -> Attempt removing from \"a\"
        if a == C[a] == 1:
            # EXPLANATION:
            #   If we remove from a chain of length \"a\", we will create something smaller than \"b\", so...
            #       The only way to be fine is to have a single element, like [1,2,2,2,3,3,3,...]
            #           -> If we had anything else, we would be stuck with a contradiction (so we move forward to removing \"b\")
            return True
        # -> Attempt removing from \"b\"
        # EXPLANATION:
        #     This only works if there is a single chain of length \"b\", and poping one element makes a chain of length \"a\".
        #     In other words, if works when \"C[b]==1 and (b-1)==a\"
        return True if (C[b] == 1 and (b - 1) == a) else False

    def remove(self, B, x):
        if B[x] == 1:
            B.pop(x)
        else:
            B[x] -= 1

    def maxEqualFreq(self, A):
        remove = self.remove
        B = Counter(A)          # Count number of repetitions/length (per value) [1,1,2,2,3,3,4] = {1:2, 2:2, 3:2, 4:1}
        C = Counter(B.values())  # Count number of times a length has been seen   [1,1,2,2,3,3,4] = { 1:1, 2:3 }
        #
        # -> Iterate Reversed, to get best answer at the first match
        for i in reversed(range(len(A))):
            # -> Check if C_dictionary is a valid answer
            if self.isvalid(C):
                return i + 1
            #
            # -> Remove current element \"x\" from our System
            x = A[i]
            # B[x] =  N_repetitions for \"x\"
            #
            remove(C, B[x])  # Deregister old N_repetitions
            remove(B, x)  # Deregister one instance of \"x\" (from N_repetitions)
            if B[x]:
                # -> If N_repetitions>0 exists, register shortened length
                C[B[x]] += 1
        return 0
