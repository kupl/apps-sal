class Solution:
    def subarrayBitwiseORs(self, A: list) -> int:
        results = set()
        pre = {0}

        for a in A:
            '''
            cur = {a}
            for prev in pre:
                cur.add(prev | a)
            results |= cur
            pre = cur
            '''
            pre = {a | p for p in pre} | {a}
            results |= pre

        return len(results)
