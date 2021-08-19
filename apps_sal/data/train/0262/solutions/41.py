class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:

        allWords = words + [result]
        firstChars = set(word[0] for word in allWords)
        maxWordLength = max(list(map(len, allWords)))

        if len(result) < maxWordLength:
            return False

        def dfs(charIdx, wordIdx, carry, visited, char2Digit):
            # check if the final sum is equal
            if charIdx == maxWordLength:
                return carry == 0

            # if we have assigned digits to all chars at the current index
            # check if the assigned values work
            if wordIdx == len(allWords):
                sums = sum(char2Digit[word[-charIdx - 1]] if charIdx < len(word) else 0 for word in words)
                sums += carry
                if sums % 10 == char2Digit[result[-charIdx - 1]]:
                    return dfs(charIdx + 1, 0, sums // 10, visited, char2Digit)
                else:
                    return False

            # if the current char index is longer than the current word, move to the next word
            currWord = allWords[-wordIdx - 1]
            if charIdx >= len(currWord):
                return dfs(charIdx, wordIdx + 1, carry, visited, char2Digit)

            # if we already have a digit assignment for the char, skip it
            currChar = currWord[-charIdx - 1]
            if currChar in char2Digit:
                return dfs(charIdx, wordIdx + 1, carry, visited, char2Digit)

            # otherwise try every possible digit
            else:
                startDigit = 1 if currChar in firstChars else 0
                for digit in range(startDigit, 10):
                    # skip previously assigned digits
                    if digit in list(char2Digit.values()):
                        continue
                    # try the assignment
                    visited.add(digit)
                    char2Digit[currChar] = digit
                    if dfs(charIdx, wordIdx, carry, visited, char2Digit.copy()):
                        return True
                    visited.remove(digit)
                return False

        return dfs(0, 0, 0, set(), {})
