class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Similar concept to jump game3, but here we need to find the minimum
        # jumps so we need to use queue instead of stack, also we need to use
        # hashmap to handle the third jump of mirror values

        # Base Case - No jumps needed
        if len(arr) == 1:
            return 0

        # Data Structure Declaration
        q = collections.deque()
        seen = set()
        hashmap = collections.defaultdict(list)
        destination = len(arr) - 1
        minJumps = 0

        # Store mirrors in hashmap
        for index, num in enumerate(arr):
            hashmap[num].append(index)

        # Traversal start points
        q.append(0)
        seen.add(0)

        # Run loop until we have values in queue
        while q:

            sizeQ = len(q)

            # Traverse the queue level by level
            for i in range(sizeQ):
                Pos = q.popleft()
                # Check for destination
                if Pos == destination:
                    return minJumps

                # Number of choices for Jumping
                nextPos = Pos + 1
                prevPos = Pos - 1
                mirrorPos = hashmap[arr[Pos]]

                # Add if nextPos is valid
                if nextPos >= 0 and nextPos < len(arr) and nextPos not in seen:
                    seen.add(nextPos)
                    q.append(nextPos)

                # Add if prevPos is valid
                if prevPos >= 0 and prevPos < len(arr) and prevPos not in seen:
                    seen.add(prevPos)
                    q.append(prevPos)

                # Add if we have mirror elements present
                if mirrorPos:
                    for val in mirrorPos:
                        if val >= 0 and val < len(arr) and val not in seen:
                            seen.add(val)
                            q.append(val)
                    # Once current element is taken into account, delete from map
                    del hashmap[arr[Pos]]
            # for every level increase the number of Jumps
            minJumps += 1
        return minJumps
