class Solution:
    def lastSubstring(self, s: str) -> str:
        n, pointer = len(s), 0  # pointer points to the char we're comparing in candidiates
        starts = list(range(n))  # starts is starting points of candidates
        while len(starts) > 1:  # more than one candidiate
            max_end = max([s[start + pointer] for start in starts if start + pointer < n])  # max val for pointer
            new_starts = []  # starts with max_end this round are filtered to compare for next round
            for i, start in enumerate(starts):
                if i > 1 and starts[i - 1] + pointer == start:
                    continue  # when prev candidate's pointer meets cur's start, cur is def less than prev
                elif start + pointer == n:
                    break  # reaches end, no valid new new val
                if s[start + pointer] == max_end:
                    new_starts.append(start)
            pointer += 1
            starts = new_starts
        return s[starts[0]:]
