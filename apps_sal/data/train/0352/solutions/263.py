class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_graph = {}
        for word in words:
            for second_word in words:
                if len(second_word) == len(word) + 1:
                    is_predecessor = True
                    second_word_counter = Counter(second_word)
                    first_word_counter = Counter(word)
                    for key, value in list(first_word_counter.items()):
                        if second_word_counter[key] < value:
                            is_predecessor = False
                            break
                    if is_predecessor:
                        if word in word_graph:
                            word_graph[word].append(second_word)
                        else:
                            word_graph[word] = [second_word]
        max_level = 1
        for key, value in list(word_graph.items()):
            queue = deque()
            queue.append((key, 1))
            visted = set()
            while queue:
                curr, level = queue.popleft()
                if level > max_level:
                    max_level = level
                if curr in word_graph:
                    for next_word in word_graph[curr]:
                        queue.append((next_word, level + 1))

        return max_level

