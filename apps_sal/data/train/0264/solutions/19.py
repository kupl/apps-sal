class Solution:
    def recurse(self, letters, arr, csum):
        keys_as_str = ''.join(sorted(letters))
        if keys_as_str not in self.visited:
            self.visited.add(keys_as_str)
            self.max_len = max(self.max_len, csum)

            for i, new_letters in enumerate(arr):
                if len(new_letters.intersection(letters)) > 0:
                    continue
                self.recurse(new_letters.union(letters), arr[:i] + arr[i + 1:], csum + len(new_letters))

    def maxLength(self, arr: List[str]) -> int:

        new_arr = []
        for word in arr:
            word_set = set(word)
            if len(word_set) == len(word):
                new_arr.append(word_set)

        self.max_len = 0
        self.visited = set()
        for i, letters in enumerate(new_arr):
            self.recurse(letters, new_arr[:i] + new_arr[i + 1:], len(letters))

        return self.max_len
