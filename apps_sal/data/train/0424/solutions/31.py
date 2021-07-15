class Solution:
    def getCoordinate(self, A: List[List[int]]):
        list_a = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    list_a.append(i*100 + j)
        return list_a
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        list_a = self.getCoordinate(A)
        list_b = self.getCoordinate(B)
        
        diff = [a - b for a in list_a for b in list_b]
        
        counter = {}
        for v in diff:
            if counter.get(v, None) == None:
                counter[v] = 1
            else:
                counter[v] += 1
        
        max_value = 0
        for key in list(counter.keys()):
            if counter[key] > max_value:
                max_value = counter[key]
        return max_value

