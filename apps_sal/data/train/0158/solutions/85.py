class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        step_list = []
        A_list = []
        for i in range(len(A)):
            A_list.append(A[i])
        states = [[A_list.copy(), 0, 0]]
        while states != []:
            state = states.pop(0)
            indictor = 0
            for i in range(state[1], len(A_list)):
                if state[0][i] != B[i]:
                    indictor = 1
                    for j in range(i + 1, len(A_list)):
                        if state[0][j] == B[i] and B[j] != state[0][j] and (B[j] == state[0][i]):
                            new_state = state[0].copy()
                            (new_state[j], new_state[i]) = (new_state[i], new_state[j])
                            states.append([new_state, i + 1, state[2] + 1])
                            break
                        elif state[0][j] == B[i] and B[j] != state[0][j]:
                            new_state = state[0].copy()
                            (new_state[j], new_state[i]) = (new_state[i], new_state[j])
                            states.append([new_state, i + 1, state[2] + 1])
                    break
            if indictor == 0:
                step_list.append(state[2])
        return min(step_list)
