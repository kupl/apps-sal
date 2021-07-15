class Solution:
    def minDays(self, n: int) -> int:
        state = set([n])
        steps = 0
        while 0 not in state:
            nstate = set()
            for x in state:
                nstate.add(x-1)
                if x%2 == 0:
                    nstate.add(x//2)
                if x%3 == 0:
                    nstate.add(x//3)
            steps += 1
            state = nstate
        return steps
