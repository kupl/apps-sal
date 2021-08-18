class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        count = {}
        for i in range(1, len(arr) + 1):
            count[i] = 0
        segment = {}
        res = -1
        for step, a in enumerate(arr):
            if a - 1 in segment and a + 1 in segment:
                count[abs(a - 1 - segment[a - 1]) + 1] -= 1
                count[abs(a + 1 - segment[a + 1]) + 1] -= 1
                count[abs(segment[a + 1] - segment[a - 1]) + 1] += 1
                left = segment[a - 1]
                right = segment[a + 1]
                del segment[a - 1]
                del segment[a + 1]
                segment[left] = right
                segment[right] = left

            elif a - 1 in segment:
                count[abs(a - 1 - segment[a - 1]) + 1] -= 1
                count[abs(a - 1 - segment[a - 1]) + 2] += 1
                left = segment[a - 1]
                right = a
                del segment[a - 1]
                segment[left] = right
                segment[right] = left

            elif a + 1 in segment:
                count[abs(a + 1 - segment[a + 1]) + 1] -= 1
                count[abs(a + 1 - segment[a + 1]) + 2] += 1
                left = a
                right = segment[a + 1]
                del segment[a + 1]
                segment[left] = right
                segment[right] = left

            else:
                count[1] += 1
                segment[a] = a

            if count[m] > 0:

                res = step + 1
        return res
