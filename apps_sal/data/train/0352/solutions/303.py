from collections import defaultdict


class Solution:
    def is_neighbor(self, s1, s2):
        ss = s1
        bs = s2
        neighbor = False

        for i in range(len(ss) + 1):
            padded_str = ss[:i] + '*' + ss[i:]

            for p1, p2 in zip(padded_str, bs):
                # print((p1 == '*' or p1 == p2))
                neighbor = (p1 == '*' or p1 == p2)
                if not neighbor:
                    break
            if neighbor:
                return neighbor

    path_len = 1

    def build_chains(self, chain_graph, start_key, visited=set(), curr_path=2):
        # print(curr_path_len, start_key)
        visited.add(start_key)
        # print(start_key, curr_path)
        for string in chain_graph[start_key] - visited:
            if string in chain_graph:
                self.build_chains(chain_graph, string, visited, curr_path + 1)
            else:
                print(('term:', string, curr_path + 1))
                self.path_len = max(self.path_len, curr_path + 1)

    def longestStrChain(self, words: List[str]) -> int:
        str_chain_graph = defaultdict(set)
        for w1 in words:
            for w2 in words:
                if len(w2) - len(w1) == 1:
                    neighbor = self.is_neighbor(w1, w2)
                    if neighbor:
                        str_chain_graph[w1].add(w2)
        # print(str_chain_graph)
        for key in str_chain_graph:
            self.build_chains(str_chain_graph, key, set(), 1)
        return self.path_len
