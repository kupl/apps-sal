class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        states = {(0, None, 0): 0}

        def count_len(d):
            if d == 0 or d == 1:
                return 0
            else:
                return len(str(d))
        for c in s:
            new_states = collections.defaultdict(lambda: float('inf'))
            for ((deletions, last_char, count), length) in states.items():
                if deletions < k:
                    new_state = (deletions + 1, last_char, count)
                    new_length = length
                    new_states[new_state] = min(new_states[new_state], new_length)
                if c == last_char:
                    new_state = (deletions, c, count + 1)
                    new_length = length - count_len(count) + count_len(count + 1)
                else:
                    new_state = (deletions, c, 1)
                    new_length = length + 1
                new_states[new_state] = min(new_states[new_state], new_length)
            states = new_states
        min_length = float('inf')
        for ((deletions, last_char, count), length) in states.items():
            if deletions == k:
                min_length = min(min_length, length)
        return min_length
