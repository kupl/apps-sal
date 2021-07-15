class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
        n = len(A)
        
        # this is increasing order of the content value
        
        idxs_sorted_by_value = sorted(range(n), key=lambda i: A[i])
        
        #print(idxs_sorted_by_value)
        
        odd_next_hops = self.get_next_hops(idxs_sorted_by_value)
        
        idxs_sorted_by_value.sort(key=lambda i: -A[i])
        
        even_next_hops = self.get_next_hops(idxs_sorted_by_value)

        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True
        
        
        for i in reversed(range(n - 1)):
            odd_next_hop, even_next_hop = odd_next_hops[i], even_next_hops[i]
            if odd_next_hop: odd[i] = even[odd_next_hop]
            if even_next_hop: even[i] = odd[even_next_hop]

        return sum(odd)

    
    
    def get_next_hops(self, idxs_sorted_by_value):
        # this is for setting the ans space
        next_hop = [None] * len(idxs_sorted_by_value)
        # setting up a new empty stack
        # this stack can only save the index number
        stack = []

        for i in idxs_sorted_by_value:
            # only extracted index value, this value following the order is 
            # according content is increasing 
            # only meet the condition, then adding into the array
            # if we cut the while ,stack is [0,2,1,3,4] saving the index numbers
            # next_hop[ ], has an under cover order, every next_hop[]
            # accord to origion array [0], [1], [2]
            # 
            while stack and stack[-1] < i:
                next_hop[stack.pop()] = i
                
            stack.append(i)
            #print(stack)
        print(stack)
        print(next_hop)
        
        return next_hop
