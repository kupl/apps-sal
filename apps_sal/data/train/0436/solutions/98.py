class Solution:
    def minDays(self, n: int) -> int:
        res = 0
        hashmap = {}
        queue = [n]
        while queue:
            new = []
            for item in queue:
                if item in hashmap:
                    continue 
                if item == 0:
                    return res
                if item%2==0:
                    new.append(item-item//2)
                if item%3 == 0:
                    new.append(item-((item//3)*2))
                hashmap[item] = res
                new.append(item-1)
            res += 1
            queue = new
        

