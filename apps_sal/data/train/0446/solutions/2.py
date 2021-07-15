class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        char_freq_map = {}
        for num in arr:
            if num in char_freq_map:
                char_freq_map[num] += 1
            else:
                char_freq_map[num] = 1
        
        freq_to_char_map = {}
        freqs = []
        for key in char_freq_map:
            if char_freq_map[key] in freq_to_char_map:
                freq_to_char_map[char_freq_map[key]].append(key)
            else:
                freqs.append(char_freq_map[key])
                freq_to_char_map[char_freq_map[key]] = [key]
        
        i = 0
        freqs.sort()
        ans = 0
        while(1):
            if k == 0:
                break
            freq = freqs[i]
            if k >= len(freq_to_char_map[freq])*freq:
                k -= len(freq_to_char_map[freq])*freq
                i += 1
            else:
                ans += len(freq_to_char_map[freq]) - k//freq
                k = 0
                i += 1
        
        print(freq_to_char_map)
        while(i < len(freqs)):
            ans += len(freq_to_char_map[freqs[i]])
            i += 1
        return ans 
