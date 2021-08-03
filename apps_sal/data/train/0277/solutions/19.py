class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        arr = [0] * (len(light) + 1)
        most_right = 0
        count = 0
        for i, num in enumerate(light):
            if num > most_right:
                arr[num] = arr[most_right] + 1
                most_right = num
            else:
                arr[most_right] += 1

            if arr[most_right] == most_right:
                count += 1

        return count
