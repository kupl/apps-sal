class Solution:

    def subarrayBitwiseORs(self, A: list) -> int:
        results = set()
        pre = {0}
        for a in A:
            '\n            cur = {a}\n            for prev in pre:\n                cur.add(prev | a)\n            results |= cur\n            pre = cur\n            '
            pre = {a | p for p in pre} | {a}
            results |= pre
        return len(results)
