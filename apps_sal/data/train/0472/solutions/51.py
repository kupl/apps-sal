class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
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
