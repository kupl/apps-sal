class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0

        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        for w1 in words:
            for w2 in words:
                if self.isPredecessor(w1, w2):
                    graph[w2].append(w1)
                    in_degrees[w1] += 1

        max_len = 1
        queue = deque([(w, 1) for w in graph if in_degrees[w] == 0])
        while queue:
            word, path_len = queue.popleft()
            for child in graph[word]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append((child, path_len + 1))

            max_len = path_len
        return max_len

    def isPredecessor(self, w1, w2):
        if len(w1) != len(w2) + 1:
            return False

        i1 = 0
        i2 = 0
        added = False
        while i1 < len(w1) and i2 < len(w2):
            if w1[i1] != w2[i2] and added:
                return False
            elif w1[i1] != w2[i2]:
                i1 += 1
                added = True
            else:
                i1 += 1
                i2 += 1

        return True
