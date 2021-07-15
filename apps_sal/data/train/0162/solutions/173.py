class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        map = {}
        
        def memo(p1, p2, map):
            #print(concatChar)
            if (p1, p2) in map:
                return map[(p1, p2)]
            else:
                if p1 == len(text1) or p2 == len(text2):
                    return 0
                if text1[p1] == text2[p2]:
                    map[(p1, p2)] = 1 + memo(p1+1, p2+1, map)
                else:
                    map[(p1, p2)] = max(memo(p1, p2+1, map), memo(p1+1, p2, map))
                
                # map[concatChar] = result
                # print(map)
                return map[(p1, p2)]
        
        return memo(0, 0, map)

