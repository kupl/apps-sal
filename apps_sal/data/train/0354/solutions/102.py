class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        states = {(None, 1): 1}
        
        for _ in range(n):
            new_states = collections.defaultdict(int)
            for state, count in list(states.items()):
                for i in range(1, 7):
                    if i == state[0]:
                        if state[1] + 1 <= rollMax[i - 1]:
                            new_states[(i, state[1] + 1)] += count
                    else:
                        new_states[(i, 1)] += count
            states = new_states
        return sum(states.values()) % (10 ** 9 + 7)

