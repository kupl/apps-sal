class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0
        for i in range(N - 1):
            v = arr[i]
            l = [v]
            for k in range(i + 1, N):
                v ^= arr[k]
                for w in l:
                    if v ^ w == w:
                        ans += 1
                l.append(v)
        return ans
