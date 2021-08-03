class Solution:
    def minJumps(self, arr: List[int]) -> int:
        connected = collections.defaultdict(list)
        _ = [connected[v].append(i) for i, v in enumerate(arr)]

        queue, pos_visited = [0], set([0])
        steps = 0

        while queue:
            next_steps = []
            for cur_pos in queue:
                if cur_pos == len(arr) - 1:
                    return steps
                next_steps += [cur_pos - 1, cur_pos + 1] + connected[arr[cur_pos]]
                connected[arr[cur_pos]].clear()
            queue = []
            for _ in next_steps:
                if _ >= 0 and _ < len(arr) and _ not in pos_visited:
                    queue.append(_)
                    pos_visited.add(_)
            steps += 1
        return steps
