class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def dist(a, b):
            # count number of differing characters
            return sum((1 if c != d else 0 for (c, d) in zip(a, b)))

        def swap(s, i, j):
            # swap ith and jth chars of string s
            # assert i != j
            if i > j:
                i, j = j, i
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        def DFS(string, k):
            # can string be swapped into problem's str `A` in `k` moves?
            if string == A:
                return True
            if k == 0:
                return False
            for i, c in enumerate(string):
                if A[i] == c:
                    continue
                # c is wrong, we need to swap a correct letter into it
                # only look for after current position to avoid double swaps
                for j in range(i, len(A)):
                    if string[j] == A[i] and A[j] != A[i]:
                        # try this swap
                        if DFS(swap(string, i, j), k - 1):
                            return True
                # return False after trying to correct the first wrong letter:
                # if there is any `k` solution, then there's a `k` solution
                # that starts on this letter
                return False

        for k in range(len(A)):
            if DFS(B, k):
                return k
