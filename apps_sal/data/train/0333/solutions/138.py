class Solution:

    def minJumps(self, arr):
        if len(arr) == 1:
            return 0
        if arr[0] == arr[-1]:
            return 1
        length = len(arr)
        if len(set(arr)) == length:
            return length - 1
        _map = defaultdict(set)
        for (i, val) in enumerate(arr):
            _map[val].add(i)
        (res, visit) = (0, set())
        seen = {0}
        (curs, other) = ({0}, {length - 1})
        while curs:
            res += 1
            thisLevel = set()
            for i in curs:
                if i - 1 > 0 and i - 1 not in seen:
                    thisLevel.add(i - 1)
                if arr[i] not in visit:
                    thisLevel |= _map[arr[i]] - seen
                    visit.add(arr[i])
                if i + 1 < length and i + 1 not in seen:
                    thisLevel.add(i + 1)
            if len(thisLevel & other) > 0:
                return res
            curs = thisLevel
            if len(curs) > len(other):
                (curs, other) = (other, curs)
            else:
                seen |= thisLevel
