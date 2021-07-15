class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maxcount = 0
        visited = {}
        for i in range(len(s)):
            for j in range(minSize, minSize+1):
                now = s[i:i+j]
                if now in visited:
                    continue
                    
                visited[now] = 1
                if i + j > len(s):
                    break
                    
                nowset = set(now)
                if len(nowset) > maxLetters:
                    break
                
                count = 1
                start = i+1
                while(start < len(s)):
                    pos = s.find(now, start)
                    if pos != -1:
                        start = pos + 1
                        count += 1
                    else:
                        break
                    
                maxcount = max(maxcount, count)
        
        return maxcount
