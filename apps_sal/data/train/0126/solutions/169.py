class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) == 0:
            return 0
        rolling_hash = 0
        letter_counts = collections.Counter()
        hash_counts = collections.Counter()
        unique_letters = set()
        n = len(s)
        for i in range(n):
            ch = s[i]
            rolling_hash = rolling_hash * 26 + ord(ch)
            letter_counts[ch] += 1
            unique_letters.add(ch)
            if i + 1 < minSize:
                continue
            if len(unique_letters) <= maxLetters:
                hash_counts[rolling_hash] += 1
            remove_letter = s[i - minSize + 1]
            rolling_hash -= ord(remove_letter) * 26 ** (minSize - 1)
            letter_counts[remove_letter] -= 1
            if letter_counts[remove_letter] == 0:
                unique_letters.remove(remove_letter)
        return max(hash_counts.values()) if len(hash_counts) else 0
