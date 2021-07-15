class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def helper(A):
            ans=[0]*len(A)
            stack=[]
            for a,i in A:
                while stack and stack[-1]<i:
                    ans[stack.pop()]=i
                stack.append(i)
            return ans
        
        odd=helper(sorted([a,i] for i,a in enumerate(A)))
        even=helper(sorted([-a,i] for i,a in enumerate(A)))
        l=len(A)
        oddjump,evenjump=[0]*l,[0]*l
        oddjump[-1]=evenjump[-1]=1
        for i in range(l-1)[::-1]:
            oddjump[i]=evenjump[odd[i]]
            evenjump[i]=oddjump[even[i]]
        return sum(oddjump)
        

