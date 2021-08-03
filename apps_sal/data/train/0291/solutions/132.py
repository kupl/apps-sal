def accumulate(arr):
    acc = 0
    for elem in arr:
        acc = (acc + elem) % 2
        yield acc


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        parity_array = (x % 2 for x in arr)
        cumulative_array = accumulate(parity_array)

        prev = [1, 0]
        ans = 0
        for elem in cumulative_array:
            ans += [prev[1], prev[0]][elem]
            prev[elem] += 1

        return ans % (10 ** 9 + 7)
