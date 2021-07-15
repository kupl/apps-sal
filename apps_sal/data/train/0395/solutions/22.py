class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n=len(A)
        next_l,next_h,dec_stack,inc_stack,nums,seen=[0]*n,[0]*n,[],[],sorted([[A[ind],ind] for ind in range(len(A))]),{}
        for num,ind in nums:
            while dec_stack and dec_stack[-1]<ind:
                next_h[dec_stack.pop()]=ind
            dec_stack.append(ind)
        nums=sorted([[-A[ind],ind] for ind in range(len(A))])
        for num,ind in nums:
            while inc_stack and inc_stack[-1]<ind:
                next_l[inc_stack.pop()]=ind
            inc_stack.append(ind)
        def is_possible(ind,jump):
            if ind==n-1:
                return True
            if (ind,jump) in seen:
                return seen[ind,jump]
            temp=False
            if jump%2:
                if next_h[ind]:
                    temp=is_possible(next_h[ind],jump+1)
            else:
                if next_l[ind]:
                    temp=is_possible(next_l[ind],jump+1)
            seen[ind,jump]=temp
            return temp
        return sum(1 for i in range(n-1,-1,-1) if is_possible(i,1))
