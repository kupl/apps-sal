from collections import Counter, defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length_to_words = defaultdict(list)

        for word in words:
            length_to_words[len(word)].append(word)

        lengths = sorted(length_to_words.keys(), reverse=True)

        successors = defaultdict(list)

        for length in lengths:
            for word in length_to_words[length]:

                for predecessor_candidate in length_to_words[length - 1]:
                    if predecessor(predecessor_candidate, word):
                        successors[predecessor_candidate].append(word)

        max_lengths = {}

        for length in lengths:
            for word in length_to_words[length]:
                if word in successors:
                    max_lengths[word] = 1 + max([max_lengths[s] for s in successors[word]])
                else:
                    max_lengths[word] = 1
        return max(max_lengths.values())


def predecessor(word1, word2):
    word1_counts = Counter(word1)
    word2_counts = Counter(word2)

    letters = set(word1 + word2)

    diff = [abs(word1_counts[l] - word2_counts[l]) for l in letters]
    nonzero_diff = [d for d in diff if d > 0]
    if len(nonzero_diff) != 1:
        return False
    if nonzero_diff[0] != 1:
        return False
    return True
