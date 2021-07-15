class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if not initialBoxes : return 0
        visited = set()
        boxes=set()
        keys_found=set()
        n_candies=0
        opn=[]
        # for i in range(len(initialBoxes)):
        for i in initialBoxes:
            if status[i]!=1:
                boxes.add(i)
            else:
                opn.append(i)
        
        initialBoxes=opn
        while initialBoxes :
            i=initialBoxes.pop(0)
            n_candies+=candies[i]
            visited.add(i)
            if keys[i] != []:
                for j in keys[i]:
                    keys_found.add(j)                            
            if containedBoxes[i] != []:
                for c in containedBoxes[i]:
                    
                    if status[c] == 1:
                        initialBoxes.append(c)
                    else:
                        boxes.add(c)
            for k in boxes:
                if k in visited:
                    continue
                if k in keys_found:
                    initialBoxes.append(k)
                    visited.add(k)
        # print(visited)
        
        return n_candies        
                
                

