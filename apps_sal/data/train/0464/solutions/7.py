class Solution:
    def minOperations(self, n: int) -> int:
        total = 0
        for i in range(n // 2):
            total += n - (2 * i + 1)
        return total

        # middle one is 2k + 1
        # first is 2*0 + 1
        # last is 2*n + 1 --> diff is 2(n-k) so around n
        # second last is 2*(n-1) + 1 --> diff is 2(n-k-1) so around n - 2
        # inds_from_end = 0
        # arr = [(2*i)+1 for i in range(n)]
        # count = 0
        # # print(arr)
        # while len(set(arr)) != 1 and inds_from_end < n//2:
        #     # print(arr, n-inds_from_end-1)
        #     while arr[inds_from_end] != arr[n-inds_from_end-1]:
        #         print(arr, count)
        #         arr[inds_from_end] += 1
        #         arr[n-inds_from_end-1] -= 1
        #         count += 1
        #     inds_from_end += 1

        return count
