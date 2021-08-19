class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        max_len = len(result)
        if max((len(w) for w in words)) > max_len:
            return False
        words = [word.rjust(max_len, '#') for word in words]
        result = result.rjust(max_len, '#')
        equations = list(zip(result, *words))
        used_digits = set()
        nonzero_chars = set(equations[0])
        assignments = {'#': 0}

        def isSAT(eqn_index, carry):
            if eqn_index < 0:
                return carry == 0
            remaining_terms = []
            for t in equations[eqn_index]:
                if t not in assignments:
                    for guess in range(10):
                        if guess in used_digits:
                            continue
                        if guess == 0 and t in nonzero_chars:
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
            else:
                return isSAT(eqn_index - 1, s // 10)
        return isSAT(max_len - 1, 0)
