class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # array to add to check values and to pop current values
        to_check = [start]

        while len(to_check) > 0:
            current = to_check.pop(0)
            if arr[current] == 0:
                return True
            if arr[current] < 0:
                continue

            for i in [current + arr[current], current - arr[current]]:
                if 0 <= i < len(arr):
                    to_check.append(i)

            arr[current] = -1

        return False

        # change = 1
        # prevchange = 0
        # n = len(arr)
        # if arr[start] == 0:
        #     return True
        # while change != prevchange:
        #     prevchange = change
        #     for index, val in enumerate(arr):
        #         print(arr)
        #         # if val is 0 then skip
        #         if val != 0:
        #         # check the jump is within bounds
        #             if index + val < n and arr[index + val] == 0 and index != start:
        #                 arr[index] = 0
        #                 change += 1
        #             elif index - val > -1 and arr[index - val] == 0 and index != start:
        #                 arr[index] = 0
        #                 change += 1
        #             elif index + val < n and arr[index + val] == 0 and index == start:
        #                 return True
        #             elif index - val > -1 and arr[index - val] == 0 and index == start:
        #                 return True
        # return False
