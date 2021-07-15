class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        tracker = collections.defaultdict(int)
        
        window_tracker = collections.defaultdict(int)
        curr_sum = 0
        
        i = 0
        j = 0
        
        while j < len(s):
            curr = s[j]
            window_tracker[curr] += 1
            curr_sum += 1
            
            # while i < j and (len(window_tracker.keys()) > maxLetters and curr_sum > minSize):
            while i < j and curr_sum > minSize:
                curr_i = s[i]
                curr_sum -= 1
                window_tracker[curr_i] -= 1
                if window_tracker[curr_i] == 0:
                    del window_tracker[curr_i]
                i += 1
            
            temp = collections.defaultdict(int)
            toAdd = s[i:j + 1]
            for char in toAdd:
                temp[char] += 1
            
            if minSize <= curr_sum <= maxSize and len(temp.keys()) <= maxLetters:
                tracker[s[i: j + 1]] += 1
            
            j += 1
        
        print(tracker)
        if len(tracker.values()) == 0:
            return 0
        return max(tracker.values())
