class Solution:

    def maxLength(self, arr: List[str]) -> int:

        def digit_representation(s):
            ans = 0
            for c in s:
                ans |= 1 << ord(c) - ord('a')
            return ans
        A = sorted([(len(s), digit_representation(s)) for s in set(arr) if len(set(s)) == len(s)], reverse=True)
        if not A:
            return 0
        R = [sum((t[0] for t in A))]
        for i in range(1, len(A)):
            R.append(R[-1] - A[i][0])
        self.ans = A[0][0]

        def helper(i, b, k):
            if i == len(A):
                self.ans = max(self.ans, k)
            elif k + R[i] > self.ans:
                if not b & A[i][1]:
                    helper(i + 1, b | A[i][1], k + A[i][0])
                helper(i + 1, b, k)
        helper(0, 0, 0)
        return self.ans
