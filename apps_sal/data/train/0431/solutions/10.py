class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        (left, right, sl, sr) = ([0] * n, [0] * n, [], [])
        for i in range(n):
            count = 1
            while sl and sl[-1][0] > A[i]:
                count += sl.pop()[1]
            left[i] = count
            sl.append([A[i], count])
        for j in range(n)[::-1]:
            count = 1
            while sr and sr[-1][0] >= A[j]:
                count += sr.pop()[1]
            right[j] = count
            sr.append([A[j], count])
        return sum((a * l * r for (a, l, r) in zip(A, left, right))) % 1000000007
