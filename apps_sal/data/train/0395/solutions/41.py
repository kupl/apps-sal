class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        #[10,13,12,14,15]
        #0，2，1，3，4
        # [2,3,3,4,N4] (makeStack for odd)
        # 4,3,1,2,0
        #[None,2,None,None,N4] (makeStack for even)

        sortA = sorted(list(range(len(A))),key=lambda i:A[i])
        oddStack = self.makeStack(sortA)
        oddStack[-1]=len(A)-1 #the current index (0 to len) can jump to where in odd step
        
        sortA = sorted(list(range(len(A))),key=lambda i:A[i],reverse=True)
        evenStack = self.makeStack(sortA)
        evenStack[-1]=len(A)-1
        print(('evenstakc',evenStack))
        print(('oddsatck',oddStack))
        # if one can jump to en at odd or even step
        odd = [False]*(len(A))
        even = [False]*(len(A))
        odd[-1]=True
        even[-1]=True
        print(('len odd',len(odd)))
        print(('len even',len(even)))
        for i in range(len(A)-2,-1,-1):
            print(('i is',i))
            if oddStack[i]:
                odd[i] = even[oddStack[i]] #if i can jump to oddStack[i], then check if even[oddStack[i]] can jump to end
            if evenStack[i]:
                even[i]=odd[evenStack[i]]
        print(odd)
        print(even)
        return sum(odd)
    def makeStack(self,sortA):
        stack=[None]*len(sortA)
        res = []
        for i in sortA:
            while res and i>res[-1]:
                stack[res.pop()]=i
            res.append(i)
        return stack
         

