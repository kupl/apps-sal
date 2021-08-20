def power_value(num: int, counter=0):
    if num % 2 == 0:
        num = num / 2
    else:
        num = 3 * num + 1
    counter += 1
    if num == 1:
        return counter
    else:
        return power_value(num, counter=counter)


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        to_sort = []
        for i in range(lo, hi + 1):
            to_sort.append([i, power_value(i)])
        to_sort = sorted(to_sort, key=lambda x: x[1])
        return to_sort[k - 1][0]
