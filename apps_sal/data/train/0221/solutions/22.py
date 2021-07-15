from functools import reduce
class Solution:
    def longestDupSubstring(self, S):
        def evaluateLength(length):
            power = pow(26, length, mod)
            current = reduce(lambda x, y: (x*26 + y) % mod, ids[:length], 0)
            explored = {current}
            for index in range(length, len(S)):
                current = (current * 26 + ids[index] - ids[index - length] * power) % mod
                if current in explored:
                    return index - length + 1
                explored.add(current)
        
        ids = [ord(character) - ord('a') for character in S]
        mod = 2**63 - 1
        index, low, high = 0, 0, len(S)
        while low < high:
            mid = (high + low + 1) // 2
            position = evaluateLength(mid)
            if position:
                index = position
                low = mid
            else:
                high = mid - 1 
        return S[index:(index+low)]

