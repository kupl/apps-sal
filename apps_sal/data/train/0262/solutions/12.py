class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        max_len = len(result)
        if max((len(w) for w in words)) > max_len:
            return False
        equations = [[result[-i - 1]] + [word[-i - 1] for word in words if i < len(word)] for i in range(max_len)]
        used_digits = set()
        nonzero_chars = set((word[0] for word in words + [result]))
        assignments = {}

        def isSAT(eqn_index, carry):
            if eqn_index >= max_len:
                return carry == 0
            remaining_terms = []
            for t in equations[eqn_index]:
                if t not in assignments:
                    for guess in range(t in nonzero_chars, 10):
                        if guess in used_digits:
                            continue
                        assignments[t] = guess
                        used_digits.add(guess)
                        if isSAT(eqn_index, carry):
                            return True
                        del assignments[t]
                        used_digits.remove(guess)
                    return False
            s = sum((assignments[c] for c in equations[eqn_index][1:])) + carry
            if s % 10 != assignments[equations[eqn_index][0]]:
                return False
            return isSAT(eqn_index + 1, s // 10)
        return isSAT(0, 0)
