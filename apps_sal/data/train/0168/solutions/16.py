class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = {}
        for char in s:
            count[char] = count.get(char,0)+1
#        print(len([char for char in count if count[char]%2==1]), count)
        return k>=len([char for char in count if count[char]%2==1]) and k<=len(s)
