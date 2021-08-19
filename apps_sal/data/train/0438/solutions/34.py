import bisect


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        last = N - 1
        groupStartWith = {0: last}
        groupEndWith = {last: 0}
        groupLength = {N: 1}

        def decreaseGroupLength(oldlen):
            if oldlen >= m:
                oldlencount = groupLength.pop(oldlen)
                if oldlencount > 1:
                    groupLength[oldlen] = oldlencount - 1

        def increaseGroupLength(newlen):
            if newlen >= m:
                if newlen in groupLength:
                    groupLength[newlen] = groupLength[newlen] + 1
                else:
                    groupLength[newlen] = 1

        def getGroup(num):
            if num in groupStartWith:
                right = groupStartWith.pop(num)
                groupEndWith.pop(right)
                return (num, right)
            elif num in groupEndWith:
                left = groupEndWith.pop(num)
                groupStartWith.pop(left)
                return (left, num)

            starts = sorted(list(groupStartWith.keys()))
            index = bisect.bisect_left(starts, num) - 1
            if index < 0:
                return ()
            left = starts[index]
            right = groupStartWith[left]
            if left <= num and num <= right:
                groupStartWith.pop(left)
                groupEndWith.pop(right)
                return (left, right)
            return ()

        def updateGroup(left, right):
            if right - left + 1 >= m:
                groupStartWith[left] = right
                groupEndWith[right] = left

        def removeNumber(num):
            group = getGroup(num)
            if len(group) == 0:
                return ()

            left, right = group
            res = ()
            oldlen = right - left + 1
            if oldlen < m:
                return ()
            decreaseGroupLength(oldlen)

            if num == left:
                newlen = oldlen - 1
                updateGroup(left + 1, right)
                increaseGroupLength(newlen)
                return (newlen,)

            if num == right:
                newlen = oldlen - 1
                updateGroup(left, right - 1)
                increaseGroupLength(newlen)
                return (newlen,)

            newLeftLen = num - left
            newRightLen = right - num

            if newLeftLen >= m:
                updateGroup(left, num - 1)
                increaseGroupLength(newLeftLen)
                res = res + (newLeftLen,)

            if newRightLen >= m:
                updateGroup(num + 1, right)
                increaseGroupLength(newRightLen)
                res = res + (newRightLen,)

            return res

        if m == N:
            return m

        for i in range(N, 0, -1):
            #print(groupStartWith, i - 1, arr[i-1] - 1)
            if m in removeNumber(arr[i - 1] - 1):
                #print(groupStartWith, i - 1, arr[i-1] - 1, '=')
                return i - 1
            #print(groupStartWith, i - 1, arr[i-1] - 1, '-')

        return - 1
