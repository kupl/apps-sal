class Solution:
    def minJumps(self, arr):

        if len(arr) == 1:
            return 0

        q = collections.deque()
        seen = set()
        hashmap = collections.defaultdict(list)
        destination = len(arr) - 1
        minJumps = 0

        for index, num in enumerate(arr):
            hashmap[num].append(index)

        q.append(0)
        seen.add(0)

        while q:

            sizeQ = len(q)

            for i in range(sizeQ):
                Pos = q.popleft()
                if Pos == destination:
                    return minJumps

                nextPos = Pos + 1
                prevPos = Pos - 1
                mirrorPos = hashmap[arr[Pos]]

                if nextPos >= 0 and nextPos < len(arr) and nextPos not in seen:
                    seen.add(nextPos)
                    q.append(nextPos)

                if prevPos >= 0 and prevPos < len(arr) and prevPos not in seen:
                    seen.add(prevPos)
                    q.append(prevPos)

                if mirrorPos:
                    for val in mirrorPos:
                        if val >= 0 and val < len(arr) and val not in seen:
                            seen.add(val)
                            q.append(val)
                    del hashmap[arr[Pos]]
            minJumps += 1
        return minJumps
