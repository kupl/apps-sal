class Solution:
    def numWays(self, s: str) -> int:
        count = s.count('1')
        
        if count % 3 != 0:
            return 0
        
        length = len(s) - 1
        if count == 0:
            return (( length ) * ( length - 1 ) // 2) % 1000000007
        
        first_range, second_range, index, curr_ones, per_triplet = 1, 1, 0, 0, count // 3
        
        while index < length:
            if s[index] == '1':
                curr_ones += 1
            elif curr_ones == per_triplet:
                first_range += 1
            elif curr_ones == 2 * per_triplet:
                second_range += 1
            
            index += 1

        return (first_range * second_range) % 1000000007
