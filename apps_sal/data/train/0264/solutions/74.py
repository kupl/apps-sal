class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.array = arr

        return max(self.recurse('', set(), 0, True), self.recurse('', set(), 0, False))

    def recurse(self, prefix: str, letters: set, index: int, include: bool):
        if index >= len(self.array):
            return len(prefix)

        if include:
            if len(self.array[index]) != len(set(self.array[index])):
                return len(prefix)

            if any(letter in letters for letter in self.array[index]):
                return len(prefix)

            return max(
                self.recurse(''.join((prefix, self.array[index])), letters | set(self.array[index]), index + 1, True),
                self.recurse(''.join((prefix, self.array[index])), letters | set(self.array[index]), index + 1, False),
            )

        return max(
            self.recurse(prefix, letters, index + 1, True),
            self.recurse(prefix, letters, index + 1, False),
        )
