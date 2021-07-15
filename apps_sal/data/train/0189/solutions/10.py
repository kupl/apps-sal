class Solution:
    
    
    def get_pair(self, i):
        for j in self.pairs:
            if i in j:
                for k in j:
                    if k != i:
                        return k
                    
                    
    def t_happy(self, t, i):
        pair = self.get_pair(t)
        for j in self.prefer[t]:
            if j == pair:
                return True
            if j == i:
                return False
                    
                    
    def happy(self, i, p):
        prefer = self.prefer[i]
        if prefer[0] == p:
            return True
        for j in range(1, len(prefer)):
            if not self.t_happy(prefer[j-1], i):
                return False
            if prefer[j] == p:
                return True

    
    
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        self.prefer = preferences
        self.pairs = pairs
        count = 0
        for i in range(n):
            p = self.get_pair(i)
            if not self.happy(i, p):
                count += 1
        return count

