'''
Start: 2:25 p.m.
'''

'''
- Visualize everything.
- Work with concrete examples.
- Commit to a hunch. Crystallize it into an approach that can be evaluated (validated/invalidated). OK if approach seems unlikely to work.
'''

'''
[16, 16]

A will not send FR to someone who is older (same age OK).
=> sort the array

A will not send FR to someone who is \"much\" younger.
If A is under 100, he will not send FR to anyone over 100.
Not FR self.
'''

'''
Brute-force: evaluate every pair
Time: O(n^2)
Space: O(1)
'''

'''
- A will not friend anyone older so no need to look forward, only backward.

Time:O(n log n)
Space: O(n)

- Sort
- For each num, compute minimum bound, BS.

lb = 16/8 + 7 = 15

[16,17,18]
 i
 
 17/2 = 8.5 ~= 8
 15
'''

'''
Test Cases
no numbers before i (works)
[5]
 i
 
 nothing >= lower bound (works)
 [1, 2, 50]
        i
        
lb = 32
multiple occurrences of lb (works)
[1, 2, 32, 32, 40, 41, 50]
       m
 l
       r
                       i
       ret
               
lb = 32
only > lb (works)
[1, 2, 40, 41, 50] 
               i
       ret
       
[40, 41, 50] (works)
         i
 ret
'''

'''
PASS
[1, 2, 32, 32, 40, 41, 50]
[1, 2, 50]
[1, 2, 40, 41, 50] 
[40, 41, 50]
[16,16]
'''

class Solution:
    def firstLTE(self, lowerBound, ages, endIndex):
        if endIndex < 0:
            return 0
        
        l = 0
        r = endIndex
        
        while l < r:
            m = (l + r) // 2  # originally ages[l], ages[r] instead of l, r -- I'm very compromised today.
            
            if ages[m] <= lowerBound:
                l = m + 1
            else:
                r = m
                
        if l <= r and ages[l] > lowerBound:
            return l
                
        return endIndex + 1
    
    def findEarliest(self, key, ages, endIndex):
        if endIndex < 0:
            return -1
        
        l = 0
        r = endIndex
        
        while l < r:
            m = (l + r) // 2
            
            if ages[m] >= key:
                r = m
            else:
                l = m + 1
        
        if l <= endIndex and ages[l] == key:
            return l
        
        return -1
    
    '''
    [16, 16]
     l
     r
         i
      
     lowerBound = 23
    [1, 2, 32, 32]
        m        
           l
           r
    '''
    
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        
        numRequests = 0
        
        ages.sort()  # O(n log n)/O(n)
        
        for i, a in enumerate(ages):
            lowerBound = a*0.5 + 7  # divided instead of multiplied originally
            startIndex = self.firstLTE(lowerBound, ages, i - 1)
            #print('i = {}, startIndex = {}, delta = {}'.format(i, startIndex, i - startIndex))
            numRequests += i - startIndex
            
            if a > lowerBound:
                startIndex = self.findEarliest(a, ages, i - 1)
                if startIndex >= 0 and startIndex < i:
                    numRequests += i - startIndex
        
        return numRequests
    
'''
[73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
'''   
        

