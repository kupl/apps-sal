class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        my_dict = {}
        for i in range(len(s) - minSize + 1):
            if len(set(s[i:i + minSize])) <= maxLetters:
                if s[i:i + minSize] in my_dict:
                    my_dict[s[i:i + minSize]] += 1
                else:
                    my_dict[s[i:i + minSize]] = 1
        # print(my_dict)
        k = minSize + 1
        if minSize != maxSize:
            while(maxSize >= k):
                for i in range(len(s) - k + 1):
                    if len(set(s[i:i + k])) <= maxLetters:
                        if s[i:i + k] in my_dict:
                            my_dict[s[i:i + k]] += 1
                        else:
                            my_dict[s[i:i + k]] = 1
                # print(my_dict)
                k += 1
        return max(my_dict.values()) if my_dict else 0
