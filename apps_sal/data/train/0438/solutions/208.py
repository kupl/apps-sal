class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        a = len(arr)
        if a == m:
            return m
        arr_set = set(arr)
        arr.reverse()
        for i in range(a):
            arr_set.remove(arr[i])
            back_i = arr[i] + 1
            if back_i in arr_set:
                cur_streak = 1
                while back_i + 1 in arr_set:
                    back_i += 1
                    cur_streak += 1
                    if cur_streak > m:
                        break
                if cur_streak == m:
                    return a - 1 - i
            front_i = arr[i] - 1
            if front_i in arr_set:
                cur_streak = 1
                while front_i - 1 in arr_set:
                    front_i -= 1
                    cur_streak += 1
                    if cur_streak > m:
                        break
                if cur_streak == m:
                    return a - 1 - i
        return -1
