# longest run that only contains two symbols?
# 6:52 -> 7:01 TLE on naive n^2 solution
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = 0
        starts = {}
        start = end = 0
        longest = 0
        
        def find_earliest(starts):
            earliest = len(tree)
            for key in starts:
                earliest = min(starts[key], earliest)
            return earliest
        
        while end < len(tree):
            # print(start, end, starts)
            current = tree[end]
            if current in starts:
                starts[current] = end
                end += 1
            else:
                if counts == 2:
                    earliest = find_earliest(starts)
                    del starts[tree[earliest]]
                    start = earliest + 1
                    counts -= 1
                else:
                    starts[current] = end
                    counts += 1
                    end += 1
            longest = max(end - start, longest)
        
        return max(end - start, longest)
        
        
#         longest = 0
        
#         def contains_two_symbols(subarray):
#             c = Counter(subarray)
#             contains = 0
#             for key in c:
#                 if c[key]:
#                     contains += 1
#             return contains < 3
            
#         for i in range(len(tree)):
#             for j in range(i + 1, len(tree) + 1):
#                 if contains_two_symbols(tree[i:j]):
#                     longest = max(longest, j - i)
        
#         return longest

