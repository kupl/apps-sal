class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        variants = [text[x:y] for (x, y) in itertools.combinations(range(len(text) + 1), r=2) if y - x > 1 and (y - x) % 2 == 0 and ((size := ((y - x) // 2)) > 0) and (text[x:x + size] == text[x + size:y])]
        return len(set(variants))
