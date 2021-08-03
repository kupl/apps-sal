class Solution:
    def coinChange(self, denoms: List[int], n: int) -> int:
        if n == 0:
            return 0
        nodes = set([0])
        seen = set()
        count = 1
        while nodes:
            seen = seen | nodes
            next_nodes = set()
            for node in nodes:
                for denom in denoms:
                    candidate = node + denom
                    if candidate == n:
                        return count
                    elif candidate < n and candidate not in seen:
                        next_nodes.add(candidate)
            count += 1
            nodes = next_nodes

        return -1
        pass
