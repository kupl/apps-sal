class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        """ correct but too slow lol :'(
        l = len(A)

        def loop(one: int, two: int, ind: int, length: int) -> int:
            if (ind == l):
                return length
            elif (one + two == A[ind]):
                #print("one, two are " + str(one) + " " + str(two))
                return loop(two, A[ind], ind + 1, length + 1)
            else:
                return loop(one, two, ind + 1, length)

        maxLen = 0

        for i in range(l):
            for j in range(i+1, l):
                c = loop(A[i], A[j], j+1, 0)
                maxLen = max(maxLen, c)

        return (maxLen + 2) if maxLen else maxLen
        """
        mySet = set(A)
        maxCount = 0
        l = len(A)
        for i in range(l):
            for j in range(i + 1, l):
                one = A[i]
                two = A[j]
                count = 0
                while one + two in mySet:
                    temp = two
                    two = one + two
                    one = temp
                    count += 1
                maxCount = max(maxCount, count)
        return maxCount + 2 if maxCount else 0
