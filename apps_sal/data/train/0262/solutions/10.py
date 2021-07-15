class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # backtracking?
        # awice ++
        words.append(result)
        R, C = len(words), max(list(map(len, words)))
        used = {}
        used_d = [None] * 10
        
        def backtrack(row, col, bal):
            if col >= C:
                return bal == 0 and all(used[w[0]] != 0 for w in words)
            if row == R:
                return bal % 10 == 0 and backtrack(0, col + 1, bal // 10)
            word = words[row]
            if col >= len(word):
                return backtrack(row + 1, col, bal)
            
            letter = word[-1 - col]
            sign = 1 if row < R - 1 else -1
            if letter in used:
                return backtrack(row + 1, col, bal + sign * used[letter])
            else:
                for d, ad in enumerate(used_d):
                    if ad is None and (d or col != len(word) - 1):
                        # start backtracking
                        used[letter] = d
                        used_d[d] = letter
                        if backtrack(row + 1, col, bal + sign * d):
                            return True
                        # restore to previous state
                        used_d[d] = None
                        del used[letter]
                        
            return False
        
        return backtrack(0, 0, 0)

