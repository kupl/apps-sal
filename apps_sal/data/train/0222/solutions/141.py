class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fibSeqs = {}
        ans = 0
        for i3 in range(1, len(arr)):
            for i2 in reversed(range(i3)):
                v1 = arr[i3] - arr[i2]
                cl = fibSeqs.get((v1, arr[i2]))
                if cl is None:
                    fibSeqs[(arr[i2], arr[i3])] = 0
                    continue

                if arr[i2] < v1:
                    break

                fibSeqs[(arr[i2], arr[i3])] = cl+1
                ans = max(ans, cl+3)

        return ans
