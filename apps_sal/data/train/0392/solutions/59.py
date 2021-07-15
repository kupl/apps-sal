# 2:52 if num ones % 3 != 0 can't be done
# identify groups, find 0s between them
# 1 00 1 00 1
# |00, 0|0, 00|
# 1 n 1 m 1
# (n + 1)*(m + 1)
# 0 0000 0 -> |0000 (|000, 0|00, 00|0, 000|), 0|000, 00|00, 000|0, 0000|
# 0 000 0 -> |0|00, |00|0, |000|, 0|0|0, 0|00|, 00|0|
class Solution:
    def numWays(self, s: str) -> int:
        count = len(list([char for char in s if char == '1']))
        if count % 3 != 0:
            return 0
    
        if count / 3 == 0:
            zeroes_in_middle = len(s) - 2
            total = 0
            for marker in range(zeroes_in_middle + 1):
                total += (zeroes_in_middle - marker) % (10**9 + 7)
            return total % (10**9 + 7)
        
        def get_zeroes(s, count):
            num_ones = 0
            zeroes = {'first': 0, 'second': 0}
            for bit in s:
                if bit == '1':
                    num_ones += 1
                else:
                    if num_ones == count:
                        zeroes['first'] += 1
                    elif num_ones == 2*count:
                        zeroes['second'] += 1
            return zeroes
                    
        
        zeroes = get_zeroes(s, count / 3)
        
        # print(zeroes)
        
        if not zeroes['first'] and not zeroes['second']:
            return 1
        elif zeroes['first'] and not zeroes['second']:
            return zeroes['first'] + 1
        elif zeroes['second'] and not zeroes['first']:
            return zeroes['second'] + 1
        
        return (zeroes['first'] + 1)*(zeroes['second'] + 1) % (10**9 + 7)

