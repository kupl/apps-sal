

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr or len(arr) == 1:
            return 0

        val_to_idxes = collections.defaultdict(list)
        adj = collections.defaultdict(set)

        for i in range(len(arr)):
            val_to_idxes[arr[i]].append(i)

        q = [(0, 0)]
        visited = {0}
        while q:
            idx, dist = q.pop(0)

            if idx == len(arr) - 1:
                return dist

            visited.add(idx)

            if idx - 1 >= 0 and (idx - 1) not in visited:
                q.append((idx - 1, dist + 1))
                visited.add(idx - 1)

            if idx + 1 < len(arr) and (idx + 1) not in visited:
                q.append((idx + 1, dist + 1))
                visited.add(idx + 1)

                if idx + 1 == len(arr) - 1:
                    return dist + 1

            for neighbor in val_to_idxes[arr[idx]]:

                if neighbor in visited:
                    continue

                q.append((neighbor, dist + 1))
                visited.add(neighbor)

                if neighbor == len(arr) - 1:
                    return dist + 1

            val_to_idxes[arr[idx]] = []

        return -1
