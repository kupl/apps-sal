class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        self.result = ['']
        self.index = 0
        def back_track(cur):
            if len(cur) == n:
                self.index+=1
                if self.index == k: 
                    self.result[0] = cur
                return
            for i in range(ord('a'), ord('d')):
                if len(cur)>0 and cur[-1]== chr(i):
                    continue
                back_track(cur+chr(i))
            return 
        back_track('')
        return self.result[0]
            
            

