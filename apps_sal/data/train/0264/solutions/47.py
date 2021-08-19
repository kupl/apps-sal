class Solution:

    def maxLength(self, arr: List[str]) -> int:
        char_freq = {}
        for i in range(len(arr)):
            char_freq[i] = set()
            for c in arr[i]:
                if c not in char_freq[i]:
                    char_freq[i].add(c)
                else:
                    del char_freq[i]
                    break
        items_count = len(char_freq)
        max_len = 0
        for i in range(1, 2 ** items_count):
            num = i
            current_set = set()
            current_len = 0
            for j in list(char_freq.keys()):
                intersect = current_set.intersection(char_freq[j])
                if num & 1 and (not intersect):
                    current_set.update(char_freq[j])
                    current_len += len(arr[j])
                    max_len = max(max_len, current_len)
                elif num & 1 and intersect:
                    break
                num >>= 1
        return max_len
