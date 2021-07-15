class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
#         N = len(A)

#         def get_next_larger_items(arr):
#             result = [None] * N
#             stack = [] 
#             for i in arr:
#                 while stack and i > stack[-1]:
#                     result[stack.pop()] = i
#                 stack.append(i)
#             return result

#         sorted_indices_increase = sorted(range(N), key = lambda i: A[i])
#         next_odd_jums = get_next_larger_items(sorted_indices_increase)        
                
#         sorted_indices_decrease = sorted_indices_increase[::-1]        
#         next_even_jumps = get_next_larger_items(sorted_indices_decrease)
        
#         print(sorted_indices_increase, sorted_indices_decrease)
#         print(next_odd_jums, next_even_jumps)
        
#         odd = [False] * N
#         even = [False] * N
#         odd[N-1] = even[N-1] = True

#         for i in range(N-2, -1, -1):
#             if next_odd_jums[i] is not None:
#                 odd[i] = even[next_odd_jums[i]]
#             if next_even_jumps[i] is not None:
#                 even[i] = odd[next_even_jumps[i]]

#         print(odd,even)
#         return sum(odd)



        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(list(range(N)), key = lambda i: A[i])
        oddnext = make(B)
        B.sort(key = lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)            

