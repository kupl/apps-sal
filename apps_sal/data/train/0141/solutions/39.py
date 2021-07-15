class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = len(people)
        if (l <= 1):
            return(1)
#        people = self.sortPeople(people)
        people.sort()
        i = 0; j = l-1; c = 0
        while i < j:
            print((i,j,c))
            if people[i] + people[j] <= limit:
                c +=1
                i +=1
                j -=1
            else:
                j -=1
                c +=1
        if i == j:
            c +=1
        return(c)
        
        
        
        
    def sortPeople(self, arr):
   #     print(arr)
        l = len(arr)
        if l <= 1:
            return(arr)
        pivot = arr[l-1]
        larr = [];rarr = []
        
        for i in range(l-1):
            if arr[i] >= pivot:
                rarr.append(arr[i])
            else:
                larr.append(arr[i])
       # print(larr + [pivot] + rarr)
        return(self.sortPeople(larr) + [pivot] + self.sortPeople(rarr))
        

