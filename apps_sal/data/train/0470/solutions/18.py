class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        from collections import Counter
        A.sort()
        c = Counter(A)
        res = 0
        pre = -1
        for i in range(len(A)):
            if A[i] == pre:
                continue
            pre = A[i]
            right = len(A) - 1
            left = i + 1
            while left < right:
                if A[i] + A[left] + A[right] < target:
                    left += 1
                elif A[i] + A[left] + A[right] > target:
                    right -= 1
                else:
                    if A[i] == A[right]:
                        num = c[A[i]] * (c[A[i]] - 1) * (c[A[i]] - 2) / 6
                    elif A[i] == A[left]:
                        num = c[A[i]] * (c[A[i]] - 1) / 2 * c[A[right]]
                    elif A[left] == A[right]:
                        num = c[A[left]] * (c[A[left]] - 1) / 2 * c[A[i]]
                    else:
                        num = c[A[i]] * c[A[left]] * c[A[right]]
                    res += num
                    tmp_pre = A[left]
                    while left < right and A[left] == tmp_pre:
                        left += 1
                    tmp_pre = A[right]
                    while left < right and A[right] == tmp_pre:
                        right -= 1
        return int(res) % (10 ** 9 + 7)
