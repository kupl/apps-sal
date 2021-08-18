class Solution:

    def isChild(self, parent, possible_child):
        for i in range(len(possible_child)):
            if possible_child[:i] + possible_child[i + 1:] == parent:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:

        graph = {}
        word_lens = [[] for _ in range(17)]
        for w in words:
            graph[w] = []
            word_lens[len(w)].append(w)

        for i in range(1, 16):
            parents = word_lens[i]
            possible_children = word_lens[i + 1]
            for p in parents:
                for c in possible_children:
                    if self.isChild(p, c):
                        graph[p].append(c)
        longest_len = 0
        visited = {}
        sorted_keys = sorted(graph.keys())
        for node in sorted_keys:
            to_visit = [(node, 1)]
            while(len(to_visit) != 0):
                cur_node, depth = to_visit.pop()
                visited[cur_node] = depth
                longest_len = max(depth, longest_len)
                for child in graph[cur_node]:
                    if child not in visited:
                        to_visit.append((child, depth + 1))
                    else:
                        if depth + 1 > visited[child]:
                            to_visit.append((child, depth + 1))
        return longest_len
