class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        arr = [0] * 5
        for item in croakOfFrogs:
            if item == 'c':
                arr[0] += 1
            elif item == 'r':
                arr[1] += 1
                for i in range(0, 1):
                    if arr[i] < arr[1]:
                        return -1
            elif item == 'o':
                arr[2] += 1
                for i in range(0, 1):
                    if arr[i] < arr[2]:
                        return -1
            elif item == 'a':
                arr[3] += 1
                for i in range(0, 1):
                    if arr[i] < arr[3]:
                        return -1
            else:
                arr[4] += 1
                for i in range(0, 1):
                    if arr[i] < arr[4]:
                        return -1
        cur = arr[0]
        for i in range(1, 5):
            if arr[i] != cur:
                return -1
        ' At this point there is a valid string '
        cur_frogs = 0
        result = float('-inf')
        p = 0
        while p < len(croakOfFrogs):
            if croakOfFrogs[p] == 'c':
                cur_frogs += 1
            elif croakOfFrogs[p] == 'k':
                cur_frogs -= 1
            result = max(cur_frogs, result)
            p += 1
        return result
