class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        max_len = len(result)
        if max(len(w) for w in words) > max_len:
            return False
        level = [[word[-i-1] for word in words if i<len(word)] for i in range(max_len)]
        level_set = [set([result[-i-1]] + level[i]) for i in range(max_len)]
        used_digits = set()
        nonzero_chars = set(word[0] for word in words + [result])
        assignments = {}
        def isSAT(eqn_index, carry):
            if eqn_index >= max_len:
                return carry == 0
            for t in level_set[eqn_index]:
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
            
            s = sum(assignments[c] for c in level[eqn_index]) + carry
            if s % 10 != assignments[result[-eqn_index-1]]:
                return False
            return isSAT(eqn_index +1, s // 10)
           
        return isSAT(0, 0)
