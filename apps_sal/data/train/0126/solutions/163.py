class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = 0
        left = 0
        right = minSize - 1
        d = {}
        length = len(s)
        unique_let = {}

        def popLetter(letter, n):
            unique_let[letter] -= 1
            if unique_let[letter] == 0:
                n -= 1
            return n

        def addLetter(letter, n):
            if unique_let.get(letter, 0) == 0:
                n += 1
            unique_let[letter] = unique_let.get(letter, 0) + 1
            return n
        for letter in s[:minSize - 1]:
            n = addLetter(letter, n)
        print(n)
        print(unique_let)
        while right < length:
            if left > 0:
                n = popLetter(s[left - 1], n)
            n = addLetter(s[right], n)
            print(n)
            if n <= maxLetters:
                d[s[left:right + 1]] = d.get(s[left:right + 1], 0) + 1
            right += 1
            left += 1
        print(d)
        if not d.values():
            return 0
        return max(d.values())
