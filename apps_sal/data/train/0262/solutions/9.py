class Solution(object):

    def isSolvable(self, words, result):
        words.append(result)
        (R, C) = (len(words), max(map(len, words)))
        assigned = {}
        assigned_inv = [None] * 10

        def search(column, row, bal):
            if column >= C:
                return bal == 0
            if row == R:
                return bal % 10 == 0 and search(column + 1, 0, bal // 10)
            word = words[row]
            if column >= len(word):
                return search(column, row + 1, bal)
            letter = word[~column]
            sign = 1 if row < R - 1 else -1
            if letter in assigned:
                if assigned[letter] or len(word) == 1 or column != len(word) - 1:
                    return search(column, row + 1, bal + sign * assigned[letter])
                return False
            else:
                for (d, ad) in enumerate(assigned_inv):
                    if ad is None and (d or len(word) == 1 or column != len(word) - 1):
                        assigned_inv[d] = letter
                        assigned[letter] = d
                        if search(column, row + 1, bal + sign * d):
                            return True
                        assigned_inv[d] = None
                        del assigned[letter]
            return False
        return search(0, 0, 0)
