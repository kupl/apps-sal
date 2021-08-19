class Solution:
    def rangeSum_ref(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            summ = 0
            for j in nums[i:]:
                summ += j
                res.append(summ)

        res.sort()
        ans = sum(res[left - 1:right])

        return int(ans % (10**9 + 7))

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(nums[k], k) for k in range(n)]
        heap.sort()

        cnt, sumV = 0, 0
        while(cnt < right):
            cnt, ele = cnt + 1, heap.pop(0)
            if cnt >= left:
                sumV += ele[0]

            # insert new element if existed.
            nk = ele[1] + 1
            if nk < len(nums):
                new_ele = (ele[0] + nums[nk], nk)
                k = len(heap) - 1
                while(k >= 0 and heap[k][0] > new_ele[0]):
                    k -= 1
                heap = heap[:k + 1] + [new_ele] + heap[k + 1:]

        return sumV % (10**9 + 7)
