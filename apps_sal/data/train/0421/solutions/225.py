class Solution:
    def lastSubstring(self, s: str) -> str:

        char_index_map = collections.defaultdict(list)
        for i in range(len(s)):
            char_index_map[s[i]].append(i)

        largeC = max(char_index_map)
        starts = {}
        for i in char_index_map[largeC]:
            starts[i] = i + 1

        while len(starts) > 1:
            to_delete = set()
            next_chars = collections.defaultdict(list)

            for start, end in list(starts.items()):
                if end == len(s):
                    to_delete.add(start)
                    continue

                next_chars[s[end]].append(start)

                if end in starts:
                    to_delete.add(end)

            next_starts = {}
            largeC = max(next_chars)
            for start in next_chars[largeC]:
                if start not in to_delete:
                    next_starts[start] = starts[start] + 1

            starts = next_starts.copy()

        for start in starts:
            return s[start:]
