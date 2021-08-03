class Solution:
    def findSubstring(self, s, words):
        if not words:
            return []
        word_len = len(words[0])
        word_set = {}
        for word in words:
            word_set[word] = word_set.get(word, 0) + 1
        scopes = [([], {}) for _ in range(word_len)]
        results = []
        for i in range(len(s)):
            word = s[i:i + word_len]
            if word in word_set:
                matched_queue, matched_counts = scopes[i % word_len]
                while matched_counts.get(word, 0) >= word_set[word]:
                    matched_counts[matched_queue.pop(0)] -= 1
                matched_queue.append(word)
                matched_counts[word] = matched_counts.get(word, 0) + 1
                if len(matched_queue) == len(words):
                    results.append(i - word_len * len(words) + word_len)
                    matched_counts[matched_queue.pop(0)] -= 1
            else:
                scopes[i % word_len] = ([], {})
        return results
