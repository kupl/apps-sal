def is_pred(w1, w2):
    skip_count = 0
    if len(w1) + 1 != len(w2):
        return False
    for i in range(0, len(w1)):
        if w1[i] == w2[i + skip_count]:
            pass
        elif skip_count == 0 and w1[i] == w2[i + 1]:
            skip_count += 1
        else:
            return False
    return True


def tests():
    assert is_pred('a', 'ab')
    assert not is_pred('a', 'a')
    assert not is_pred('a', 'bc')
    assert not is_pred('ab', 'a')


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        chains = {}
        current_max = 0
        for w in words:
            chains[w] = 1
            current_max = max(current_max, 1)
            word_max = 1
            for (chain, chain_len) in list(chains.items()):
                if is_pred(chain, w) and word_max < chain_len + 1:
                    chains[w] = chain_len + 1
                    word_max = chain_len + 1
                    current_max = max(current_max, word_max)
        return current_max
