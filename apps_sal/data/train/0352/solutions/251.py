class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        from collections import defaultdict, deque
        hash_map = defaultdict(list)

        max_len = 0
        q = deque()
        for char in words:
            if len(char) >1:
                neighbors = [char[:i] + char[i+1:] for i in range(len(char))]
                for n in neighbors:
                    hash_map[n].append(char)
            hash_map[char].append(char)

        for c in words:
            visited = {}
            q.append((c, 1))
            while q:
                char, count = q.pop()
                if char not in visited and char in hash_map:
                    max_len = max(max_len, count)
                    for n in hash_map[char]:
                        q.append((n, count + 1))

                visited[char] = 1
        return max_len
                    


