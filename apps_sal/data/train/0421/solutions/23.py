# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         #给的提示是用后缀树
#         #因为必定是后缀才满足最后一个字典序
#         #当然也包括它本身
#         #字典序就是下一个比它大的数或者字符串，可以有环，环首是最小的
        
        
        
        
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, indexes = 0, list(range(len(s)))
        while len(indexes) > 1:
            new = []
            mx = max([s[i + j] for j in indexes if i + j < len(s)])
            for k, j in enumerate(indexes):
                if k - 1 >= 0 and indexes[k - 1] + i == j:
                    continue
                if i + j >= len(s):
                    break
                if s[i + j] == mx:
                    new.append(j)
            i += 1
            indexes = new
        return s[indexes[0]:]
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = defaultdict(list)
#         cur = 'a'
#         for idx, val in enumerate(s):
#             if cur < val:
#                 cur = val
#             graph[val].append(idx)
        
#         maxstartst = graph[cur]
#         rt = ''
#         nxt = ord(cur)
#         end = ord('a')
#         while nxt >= end:
#             nxtchar = chr(nxt)
#             if nxtchar in graph:
#                 for item in graph[nxtchar]:
#                     temp = bisect.bisect_right(maxstartst, item-1)
#                     if maxstartst[temp-1] == item -1:
#                         return s[maxstartst[temp-1]:]
            
#             nxt-=1

#         return rt

