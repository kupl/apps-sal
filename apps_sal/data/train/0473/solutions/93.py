class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        if not arr:
            return 0

        x = [0, arr[0]]
        for i in range(1, len(arr)):
            x.append(x[-1] ^ arr[i])

        cnt = 0
        for i in range(1, len(x)):
            for j in range(i + 1, len(x)):
                for k in range(j, len(x)):
                    if x[j - 1] ^ x[i - 1] == x[k] ^ x[j - 1]:
                        cnt += 1
        return cnt
