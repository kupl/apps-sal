from collections import defaultdict

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        cand = defaultdict(lambda: [set(), set()])
        stack, stack_dec = [], []
        for x, i in sorted([(x, i) for i, x in enumerate(A)]):
            while len(stack) > 0 and stack[-1][1] < i:
                cand[i][0].add(stack.pop()[1])
            stack.append((x, i))
        for x, i in sorted([(x, i) for i, x in enumerate(A)], key=lambda y: (-y[0], y[1])):
            while len(stack_dec) > 0 and stack_dec[-1][1] < i:
                cand[i][1].add(stack_dec.pop()[1])
            stack_dec.append((x, i))
        
        n = len(A)
        ans = {n - 1}
        for_odd, for_even = {n - 1}, {n - 1}
        time = 0
        
        while len(for_odd) > 0 or len(for_even) > 0:
            time += 1
            new_odd, new_even = set(), set()
            for x in for_odd:
                for y in cand[x][1]:
                    new_even.add(y)
            for x in for_even:
                for y in cand[x][0]:
                    new_odd.add(y)
            for x in new_odd:
                ans.add(x)
            for_odd, for_even = new_odd, new_even
        
        return len(ans)

