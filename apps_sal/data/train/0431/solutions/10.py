class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left, right, sl, sr = [0] * n, [0] * n, [], []
        # left[i] is num of subarray left of A[i] with A[i] being the min
        for i in range(n):
            count = 1
            while sl and sl[-1][0] > A[i]:
                count += sl.pop()[1]
            left[i] = count
            sl.append([A[i], count])
        # right[i] is the num subarray right of A[i] with A[i] being the min
        for j in range(n)[::-1]:
            count = 1
            while sr and sr[-1][0] >= A[j]:
                count += sr.pop()[1]
            right[j] = count
            sr.append([A[j], count])
        # print(left,right)
        return sum(a * l * r for a, l, r in zip(A, left, right)) % 1_000_000_007
        

