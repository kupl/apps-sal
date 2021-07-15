class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = collections.Counter(ages)
        return sum(self.sendFriend(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)
        
    
    def sendFriend(self,A,B):
        if B <= 0.5*A+7:
            return False
        if B > A:
            return False
        if B >100 and A<100:
            return False
        return True
        

