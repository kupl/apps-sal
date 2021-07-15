class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        val = 0
        result = 0
        table = dict()
        for i in range(len(hours)):
            hour = hours[i]
            if hour > 8:
                val += 1
            else:
                val -= 1
                
            if val > 0:
                result = i + 1
            else:
                if val not in table:
                    table[val] = i
                if val - 1 in table:
                    dist = i - table[val - 1]
                    if dist > result:
                        result = dist
        
        return result
