def find_latest_step(arr, group_size):
    n = len(arr)
    left_end = [-1] * (n + 2)
    right_end = [-1] * (n + 2)
    value = [0] * (n + 2)

    def merge(a, b, removes, appends):
        if value[a] == 0 or value[b] == 0:
            return
        (lend, rend) = (left_end[a], right_end[b])
        removes.append(a - lend + 1)
        removes.append(rend - b + 1)
        appends.append(rend - lend + 1)
        left_end[rend] = lend
        right_end[lend] = rend
    right_size_group_count = 0
    latest_step = -1
    step = 1
    for elem in arr:
        removes = []
        appends = [1]
        value[elem] = 1
        left_end[elem] = elem
        right_end[elem] = elem
        merge(elem - 1, elem, removes, appends)
        merge(elem, elem + 1, removes, appends)
        right_size_group_count += -sum((1 for x in removes if x == group_size)) + sum((1 for x in appends if x == group_size))
        if right_size_group_count > 0:
            latest_step = max(latest_step, step)
        step += 1
    return latest_step


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        return find_latest_step(arr, m)
