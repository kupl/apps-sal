class Solution:
    def getArraysx (self, arr,target):
        leftSizes = {}
        rightSizes = {}  #include start-range
        posleft = 0
        posright = 0
        currSum = 0
        while  posright < len(arr):
            currSum += arr[posright]
            if currSum  == target:
                #update rifht of i, including i
                rightList = rightSizes.get(posleft,[])
                rightList.append(posright-posleft + 1)
                rightSizes[posleft] = rightList
                #update left of i, not including i
                if (posright +1 < len(arr)):
                    leftList = leftSizes.get(posright+1,[])
                    leftList.append(posright-posleft + 1)
                    leftSizes[posright+1]=leftList
                #move pointers to the right
                posright +=1
                currSum -= arr[posleft]
                posleft +=1
            elif currSum  > target:
                #remove leftmost element 
                currSum =  currSum - arr[posright] - arr[posleft] 
                posleft +=1
            else: #currSum < target
                #include current element move right pointer
                posright +=1
        #print ('left', leftSizes)   
        #print('right', rightSizes)
        leftArray = [0]*len(arr)
        fullList = []
        for i in range(len(arr)):
            additional = leftSizes.get(i,[])
            fullList.extend(additional)
            if len(fullList) > 0:
                leftArray[i] = min(fullList)
            else:
                leftArray[i] = -1
            
        rightArray = [0]*len(arr)
        fullList = []
        for j in range(len(arr)-1, -1,-1):
            additional = rightSizes.get(j,[])
            fullList.extend(additional)
            if len(fullList) > 0:
                rightArray[j] = min (fullList)
            else:
                rightArray[j] = -1
                
        return leftArray, rightArray
    
    def updateArrays (self, leftSizes, rightSizes, posleft, posright,maxvalue):
        # 3 4 5
        # 1 3 2.    target = 6
        # update i  =3  for right or equal of 3
        # update i = 6 for left of 6
        
        #update rifht of i, including i
        value = rightSizes.get(posleft,maxvalue)
        rightSizes[posleft] = min (value,posright-posleft + 1 )
        #update left of i, not including i
        if posright +1 < maxvalue:
            value = leftSizes.get(posright+1,maxvalue)
            leftSizes[posright+1]=min (value,posright-posleft + 1  )
    
    def getArrays (self, arr,target):
        leftArray = [0]*len(arr)
        rightArray = [0]*len(arr)
        leftSizes = {}
        rightSizes = {}  #include start-range
    
        posleft = 0
        posright = 0
        currSum = 0
        while  posright < len(arr):
            currSum += arr[posright]
            if currSum  == target:
                self.updateArrays(leftSizes,rightSizes, posleft, posright, len(arr))
                #move pointers to the right
                posright +=1
                currSum -= arr[posleft]
                posleft +=1
            elif currSum  > target:
                #remove leftmost element 
                currSum =  currSum - arr[posright] - arr[posleft] 
                posleft +=1
            else: #currSum < target
                #include current element move right pointer
                posright +=1
        #print ('left', leftSizes)   
        #print('right', rightSizes)
        leftArray = [len(arr)]*len(arr)
        for i in range(1,len(arr)):
            minValue = leftSizes.get(i,len(arr))
            leftArray[i] = min(minValue, leftArray[i-1])
            
        rightArray = [len(arr)]*len(arr)
        for j in range(len(arr)-1, -1,-1):
            minValue = rightSizes.get(j,len(arr))
            if j == len(arr)-1:
                rightArray[j] = minValue
            else:    
                rightArray[j] = min (minValue, rightArray[j+1])

                
        return leftArray, rightArray
    
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        leftArray, rightArray = self.getArrays ( arr,target)
        #print ('left', leftArray)
        #print ('right', rightArray)  
        #process hashmaps by i position
        minSum = 2*len(arr)
        for i in range (1,len(arr)):
            if leftArray[i] < len(arr):
                leftSize = leftArray[i]
            else:
                continue
            if rightArray[i] < len(arr):
                rightSize = rightArray[i]
            else:
                continue
            #print (i, leftSize, rigthSize)
            minSum = min(minSum, leftSize + rightSize)
        if minSum == 2*len(arr):
            minSum = -1
        return minSum
            
                

            
        
        
    def minSumOfLengthsx(self, arr: List[int], target: int) -> int:
        #two pointers 
        #loop until sum = target or > target
        #if greather than target, move posleft one to the right 

        #keep array of lenghts and get the samllet two (this can be optimized)
        #or get subarrays, even if they overlap, and then choose the smalles when overalp 
        
        posleft = 0
        posright = 0
        lengths = [] # keeping two smallest?
        currSum = 0
        while  posright < len(arr):
            currSum += arr[posright]
            #`print (posleft, posright, currSum)
            if currSum  == target:
                lengths.append(posright-posleft + 1)
                posright +=1
                posleft = posright
                currSum = 0
                #if posright < len(arr):
                #   currSum = arr[posright]
                
            elif currSum  > target:
                #remove leftmost element 
                currSum =  currSum - arr[posright] - arr[posleft] 
                posleft +=1
            else:
                #include current element move right pointer
                posright +=1
                #if posright < len(arr):
                #    currSum += arr[posright]
        print(lengths)
        if len(lengths) < 2:
            return -1
        lengths.sort()
        return sum(lengths[0:2])
            
            

