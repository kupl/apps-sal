class Solution:
    def numSplits(self, s: str) -> int:
        # stores
        unique_chars = {}
        for i, char in enumerate(s):
            if char in unique_chars:
                first, last = unique_chars[char]
                unique_chars[char] = (first, i)
            else:
                unique_chars[char] = (i, i)
        n_unique_chars = len(list(unique_chars.keys()))
        events = []
        for start, end in list(unique_chars.values()):
            events.append((start, 1))
            events.append((end, -1))
        events.sort(key=lambda x: x[0])

        left_num = 0
        right_num = n_unique_chars
        total = 0
        start_good = None
        # print(events)
        for i, event_type in events:
            #print(i, event_type, left_num, right_num)
            if start_good is not None:
                return i - start_good
            if event_type == 1:
                left_num += 1
            else:
                right_num -= 1
            if left_num == right_num:
                start_good = i
