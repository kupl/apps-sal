class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        d = dict()
        arr = []
        key = []
        for i in range(0,len(status)):
            arr.append(-1)
            key.append(-1)
            d[i] = [status[i],candies[i],keys[i],containedBoxes[i]]
            if status[i]==1:
                key[-1]=1
            
        c = 0
        res = []
        while 1!=-1:
            tmp = []
            for x in initialBoxes:
                if arr[x]==-1 and key[x]==1:
                    arr[x]=1
                    c+=d[x][1]
                    for y in d[x][2]:
                        key[y]=1
                    for y in d[x][3]:
                        if key[y]==1:
                            tmp.append(y)
                        else:
                            res.append(y)
                elif key[x]==-1:
                    res.append(x)
            initialBoxes = []
            for y in res:
                if key[y]==1 and arr[y]==-1:
                    initialBoxes.append(y)
            initialBoxes+=tmp
            if initialBoxes==[]:
                break
        return c

