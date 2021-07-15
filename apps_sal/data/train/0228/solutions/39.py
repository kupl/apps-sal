def window_sums(bits, width):
    coll = []
    pointer = 0
    total = 0
    for elem in bits:
        if len(coll) < width:
            coll.append(elem)
            total += elem
            if len(coll) == width:
                yield total
        else:
            total += elem - coll[pointer]
            coll[pointer] = elem
            pointer = (pointer + 1) % width
            yield total

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        bits = (ch in 'aeiou' for ch in s)
        sums = window_sums(bits, k)
        return max(sums)
