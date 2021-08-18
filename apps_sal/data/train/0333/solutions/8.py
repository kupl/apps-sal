class Solution:
    def minJumps(self, arr: List[int]) -> int:

        val_to_ids = collections.defaultdict(list)
        _ = [val_to_ids[x].append(i) for i, x in enumerate(arr)]

        queue = collections.deque([(0, 0)])
        positions_seen = set()
        num_met = set()
        while queue:
            i, dis = queue.popleft()
            if i == len(arr) - 1:
                return dis
            val = arr[i]
            positions_seen.add(i)

            possible_indexes = []
            possible_indexes.append(i + 1)
            possible_indexes.append(i - 1)

            if len(val_to_ids[val]) > 1:
                for idx in val_to_ids[val]:
                    if idx not in positions_seen:
                        possible_indexes.append(idx)
                del val_to_ids[val]

            for p in possible_indexes:
                if p < 0 or p > len(arr) or p in positions_seen:
                    continue
                queue.append((p, dis + 1))
