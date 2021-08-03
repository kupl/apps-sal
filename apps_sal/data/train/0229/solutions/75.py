class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counter = collections.Counter(A)
        for e in sorted(A, key=abs):
            if 2 * e in counter and counter[2 * e] > 0 and counter[e] > 0:
                counter[e] -= 1
                counter[2 * e] -= 1
        print(counter)
        return sum(counter.values()) == 0
