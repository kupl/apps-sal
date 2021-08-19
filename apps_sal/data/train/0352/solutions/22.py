class Solution:

    def can_convert(self, word1, word2):
        for missing_idx in range(len(word2)):
            if word2[:missing_idx] + word2[missing_idx + 1:] == word1:
                return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        words_by_length = collections.defaultdict(list)
        for (idx, word) in enumerate(words):
            words_by_length[len(word)].append(idx)
        adj_list = collections.defaultdict(list)
        indegree = [0] * len(words)
        for length in words_by_length:
            if length + 1 in words_by_length:
                for word_1_idx in words_by_length[length]:
                    for word_2_idx in words_by_length[length + 1]:
                        if self.can_convert(words[word_1_idx], words[word_2_idx]):
                            adj_list[word_1_idx].append(word_2_idx)
                            indegree[word_2_idx] += 1
        queue = collections.deque([word_idx for word_idx in range(len(words)) if indegree[word_idx] == 0])
        max_length = 0
        while queue:
            length = len(queue)
            max_length += 1
            for i in range(length):
                curr_word_idx = queue.popleft()
                for successor in adj_list[curr_word_idx]:
                    indegree[successor] -= 1
                    if indegree[successor] == 0:
                        queue.append(successor)
        return max_length
