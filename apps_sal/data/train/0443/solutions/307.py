class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i, r in enumerate(rating):
            if i >= len(rating) - 2:
                break
            
            # check asc
            li = [val for val in rating[i + 1:] if val > r]
            for j, r2 in enumerate(li):
                li2 = [val for val in li[j + 1:] if val > r2]
                cnt += len(li2)
                
#                 if li2:
#                     print(r, r2, li2)
            
            # if li:
            #     cnt += self.count_comb(li, r, True)
            
            # check desc
            li = [val for val in rating[i + 1:] if val < r]
            for j, r2 in enumerate(li):
                li2 = [val for val in li[j + 1:] if val < r2]
                cnt += len(li2)
            
#                 if li2:
#                     print(r, r2, li2)
            
            # if li:
            #     cnt += self.count_comb(li, r, False)
            
        return cnt
    
    
    def count_comb(self, li, num, asc):
        cnt = 0
        
        for i, r in enumerate(li):
            if i >= len(li) - 1:
                break
            
            if asc:
                for j in range(i + 1, len(li)):
                    if num < li[j]:
                        cnt += 1
            else:
                for j in range(i + 1, len(li)):
                    if num > li[j]:
                        cnt += 1

        return cnt
        
            

