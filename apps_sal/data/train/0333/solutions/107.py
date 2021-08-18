
class Solution:
    def minJumps(self, arr):
        length = len(arr)
        if len(set(arr)) == length:
            return length - 1
        if arr[0] == arr[-1]:
            return 1

        _map = defaultdict(set)
        for i, val in enumerate(arr):
            _map[val].add(i)

        res, seen, visit = 0, {0}, set()
        curs, other = {0}, {length - 1}
        while curs:
            res += 1

            thisLevel = set()
            for i in curs:
                if i - 1 > 0 and i - 1 not in seen:
                    thisLevel.add(i - 1)
                if arr[i] in _map:
                    thisLevel |= (_map[arr[i]] - seen)
                    visit.add(arr[i])
                    del _map[arr[i]]
                if i + 1 < length and i + 1 not in seen:
                    thisLevel.add(i + 1)

            if thisLevel & other:
                return res
            curs = thisLevel
            if len(curs) > len(other):
                curs, other = other, curs
            else:
                seen |= thisLevel
