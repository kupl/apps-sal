from collections import defaultdict


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        length = defaultdict(list)
        for s in words:
            length[len(s)].append(s)
        record = sorted(list(length.items()), reverse=True)
        result = defaultdict(int)
        max_length = 1
        for item in record:
            for word in item[1]:
                if result[word] == 0:
                    result[word] += 1
                for i in range(len(word)):
                    new_string = word[0:i] + word[i + 1:]
                    if new_string in words:
                        result[new_string] = max(result[new_string], result[word] + 1)
                        max_length = max(max_length, result[new_string])
        return max_length
