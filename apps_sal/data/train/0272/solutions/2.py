class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        reachable = [False for _ in status]
        for i in initialBoxes:
            reachable[i] = True
        can_open = [val == 1 for val in status]
        nodes_to_visit = [b for b in range(len(status)) if reachable[b] and can_open[b]]
        total_candies = 0
        while len(nodes_to_visit) >= 1:
            curr_node = nodes_to_visit[0]
            nodes_to_visit = nodes_to_visit[1:]
            total_candies += candies[curr_node]
            for k in keys[curr_node]:
                if not can_open[k] and reachable[k]:
                    nodes_to_visit.append(k)
                can_open[k] = True
            for b in containedBoxes[curr_node]:
                if not reachable[b] and can_open[b]:
                    nodes_to_visit.append(b)
                reachable[b] = True
        return total_candies
