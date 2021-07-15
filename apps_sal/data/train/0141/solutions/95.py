class Solution:
    
    def numRescueBoats(self, people, limit):
        people.sort()
        
        i, j = 0, len(people)-1
        ans = 0
        while i<=j:
            ans += 1
            if people[i] + people[j] <= limit:
                i+= 1
            j -= 1
        
        return ans
        
        
    def numRescueBoats2(self, people: List[int], limit: int) -> int:
        
        self.ans = 9999
        visited = [0 for _ in range(len(people)+1)]
        
        def traverse(ind:int, boatCnt:int, boats):
            if visited[ind]:
                return
            if ind == len(people):
                if boatCnt+1 < self.ans:
                    print(boats)
                    self.ans = boatCnt+1
            else:
                visited[ind] = 1
                for i in range(ind+1, len(people)+1):
                    b = boats[:]
                    if boatCnt >= len(b):
                        b.append([])

                    if sum(b[boatCnt]) + people[ind] > limit:
                        boatCnt += 1
                        if boatCnt >= len(b):
                            b.append([])
                    b[boatCnt].append(people[ind])
                    traverse(ind+1, boatCnt, b)
                visited[ind] = 0
        
        traverse(0, 0, [])
        
        #print(boats)
        return self.ans
