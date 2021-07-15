class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res=0
        record = []
        #rec = []
        for i in range(0,len(rating)):
            record.append([])
            for j in range(i+1):
                record[i].append(None)
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    record[i].append(True)
                elif rating[j] < rating[i]:
                    record[i].append(False)
        for i in range(0,len(rating)-1):

            for j in range(i+1,len(rating)):
                if record[i][j]:
                    for k in range(j+1,len(rating)):
                        if record[j][k]:
                            res += 1
                            #rec.append((rating[i],rating[j],rating[k]))
                elif record[i][j]==False:
                    for k in range(j+1,len(rating)):
                        if record[j][k]==False:
                            res += 1
                            #rec.append((rating[i], rating[j], rating[k]))
        
        return res

