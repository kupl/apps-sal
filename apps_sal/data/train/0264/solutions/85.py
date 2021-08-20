class Solution(object):

    def maxLength(self, A):
        for i in range(len(A) - 1, -1, -1):
            if len(set(A[i])) != len(A[i]):
                A.pop(i)
        N = len(A)
        B = []
        for word in A:
            ct = [0] * 26
            for letter in word:
                ct[ord(letter) - ord('a')] += 1
            B.append(ct)
        self.ans = 0
        count = [0] * 26

        def search(i):
            if i == N:
                cand = sum(count)
                if cand > self.ans:
                    self.ans = cand
                return
            for (letter, ct) in enumerate(B[i]):
                if ct and count[letter]:
                    search(i + 1)
                    break
            else:
                search(i + 1)
                for (letter, ct) in enumerate(B[i]):
                    if ct:
                        count[letter] += 1
                search(i + 1)
                for (letter, ct) in enumerate(B[i]):
                    if ct:
                        count[letter] -= 1
        search(0)
        return self.ans
