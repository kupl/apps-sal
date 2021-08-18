class Solution:
    def minSumOfLengthsOld(self, arr: List[int], target: int) -> int:
        n = len(arr)
        if n == 1:
            return -1
        i = 0
        j = 0
        sum_ = arr[i]
        interval = []
        while i < n and j < n:
            if sum_ == target:
                interval.append([i, j, (j - i + 1)])
                sum_ -= arr[i]
                i += 1
                j += 1
                if j < n:
                    sum_ += arr[j]
            elif sum_ < target:
                if j < n - 1:
                    sum_ += arr[j + 1]
                j += 1
            else:
                sum_ -= arr[i]
                i += 1
        if len(interval) == 0:
            return -1

        interval.sort(key=lambda x: x[2])
        interval_val_sorted = [x for x in interval]
        interval.sort(key=lambda x: x[0])
        '''
        for i in range(len(interval)):
            s, e, val = interval_val_sorted[i][0], interval_val_sorted[i][1], interval_val_sorted[i][2]
            ind = findCeil(e, interval)
            if ind == -1:
                continue
            val1 = ind[2]
            return val + val1
        '''
        print(interval_val_sorted)
        print(interval)
        i_, j_, l_ = interval[0][0], interval[0][1], interval[0][2]
        found = False
        for i in range(1, len(interval), 1):

            i_1, j_1, l_1 = interval[i][0], interval[i][1], interval[i][2]
            if i_1 >= i_ and i_1 <= j_:
                continue
            if i_ >= i_1 and i_ <= j_1:
                continue
            found = True
            break
        if found == False:
            return -1
        return l_ + l_1

    def findCeil(self, x, starts):
        s = 0
        e = len(starts) - 1
        res = -1
        while s <= e:
            mid = s + (e - s) // 2
            if starts[mid] > x:
                res = mid
                e = mid - 1
            else:
                s = mid + 1
        return res

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        i = 0
        j = 0
        overlaps = list()
        sum_ = 0
        j = 0
        while i < n and j < n:

            sum_ += arr[j]

            while j < n - 1 and sum_ < target:
                j += 1
                sum_ += arr[j]

            if sum_ == target:
                overlaps.append([i, j])

            sum_ -= arr[i]
            sum_ -= arr[j]
            i += 1
        if sum_ == target:
            if i <= n - 1:
                overlaps.append([i, j - 1])

        starting = [x for [x, y] in overlaps]
        length = [y - x + 1 for [x, y] in overlaps]
        l_o = len(length)
        if l_o == 0:
            return -1
        min_arr = [length[-1]]
        s = 1
        min_ = length[-1]
        for i in range(l_o - 2, -1, -1):
            min_ = min(length[i], min_)
            min_arr.append(min_)

        min_length = sys.maxsize
        min_arr = list(reversed(min_arr))
        for overlap in overlaps:
            s, e = overlap[0], overlap[1]
            indi = self.findCeil(e, starting)
            if indi == -1:
                continue
            min_length = min(min_length, e - s + 1 + min_arr[indi])
        if min_length == sys.maxsize:
            return -1

        return min_length
