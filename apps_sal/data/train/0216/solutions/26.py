class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = 'croak'
        croak_positions = {char: 0 for char in croak}
        max_size = 0
        completed = 0
        for char in croakOfFrogs:
            if char in croak_positions:
                croak_positions[char] += 1
            else:
                return -1
            for (char, count) in croak_positions.items():
                if char != croak[0]:
                    diff = croak_positions[croak[0]] - count
                    if diff < 0:
                        return -1
                    if diff > max_size:
                        max_size = diff
        for (char, count) in croak_positions.items():
            if count != croak_positions[croak[0]]:
                return -1
        return max_size
