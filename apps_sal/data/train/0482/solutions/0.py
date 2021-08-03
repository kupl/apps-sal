class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0

        res = []

        while len(arr) > 1:
            temp_res = []
            temp_res = [arr[i] * arr[i + 1] for i in range(len(arr) - 1)]
            idx = temp_res.index(min(temp_res))

            res.append(temp_res[idx])
            arr.pop(idx if arr[idx] < arr[idx + 1] else idx + 1)

            # left = arr[0] * arr[1]
            # right = arr[-1] * arr[-2]
            # if left < right:
            #     res.append(left)
            #     arr.pop(1 if arr[1] < arr[0] else 0)
            # elif right < left:
            #     res.append(right)
            #     arr.pop(-2 if arr[-2] < arr[-1] else -1)
            # else:
            #     res.append(left)
            #     if max(arr[0], arr[1]) > max(arr[-1], arr[-2]):
            #         arr.pop(-2 if arr[-2] < arr[-1] else -1)
            #     else:
            #         arr.pop(1 if arr[1] < arr[0] else 0)

        return sum(res)
