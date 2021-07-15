class Solution:
    # bidirectional, best 416 ms, memory 99.90%
    def minJumps(self, arr):
        length = len(arr)
        # if no any connection in nodes, answer equals to array length
        if len(set(arr)) == length: return length - 1
        if arr[0] == arr[-1]: return 1

        _map = defaultdict(set) # connection map
        for i, val in enumerate(arr): _map[val].add(i)

        # BFS, seen: visited index, visit: visited connection
        res, seen, visit = 0, {0}, set()
        # curs: nodes in current side level, other: nodes in opposite side
        curs, other = {0}, {length - 1}
        while curs:
            res += 1
            # store found nodes in this level
            thisLevel = set()
            for i in curs:
                # check move backwards 
                if i - 1 > 0 and i - 1 not in seen: 
                    thisLevel.add(i - 1)
                # check in place
                if arr[i] not in visit: # here can change into \"arr[i] in _map: del _map[arr[i]]\"
                    thisLevel |= (_map[arr[i]] - seen) 
                    visit.add(arr[i])
                # check move forwards
                if i + 1 < length and i + 1 not in seen: 
                    thisLevel.add(i + 1)

            # check if this level and the other side intersect
            if thisLevel & other: return res  

            # update current side for next round          
            curs = thisLevel
            # choose smaller side into next round 
            if len(curs) > len(other): curs, other = other, curs
            # if we don't exchange, put found nodes into seen
            # because they are found in current direction
            else: seen |= thisLevel
