class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}
        src_q = []
        src_visited = set()
        tgt_q = []
        tgt_visited = set()
        src_q.append((source[0], source[1]))
        tgt_q.append((target[0], target[1]))
        while src_q and tgt_q:
            (src_node_x, src_node_y) = src_q.pop(0)
            (tgt_node_x, tgt_node_y) = tgt_q.pop(0)
            if (src_node_x, src_node_y) in tgt_visited:
                return True
            if (tgt_node_x, tgt_node_y) in src_visited:
                return True
            if len(tgt_visited) > 20000 or len(src_visited) > 20000:
                return True
            if (src_node_x, src_node_y) not in src_visited:
                src_visited.add((src_node_x, src_node_y))
                src_neighboring_nodes = [(src_node_x, src_node_y - 1), (src_node_x, src_node_y + 1), (src_node_x - 1, src_node_y), (src_node_x + 1, src_node_y)]
                for each_node in src_neighboring_nodes:
                    if 0 <= each_node[0] < 10 ** 6 and 0 <= each_node[1] < 10 ** 6 and (each_node not in blocked) and (each_node not in src_visited):
                        src_q.append((each_node[0], each_node[1]))
            if (tgt_node_x, tgt_node_y) not in tgt_visited:
                tgt_visited.add((tgt_node_x, tgt_node_y))
                tgt_neighboring_nodes = [(tgt_node_x, tgt_node_y - 1), (tgt_node_x, tgt_node_y + 1), (tgt_node_x - 1, tgt_node_y), (tgt_node_x + 1, tgt_node_y)]
                for each_node in tgt_neighboring_nodes:
                    if 0 <= each_node[0] < 10 ** 6 and 0 <= each_node[1] < 10 ** 6 and (each_node not in blocked) and (each_node not in tgt_visited):
                        tgt_q.append((each_node[0], each_node[1]))
        return False
