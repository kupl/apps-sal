class Solution:

    memo = {}
    next_memo = {}
    
    def get_next_move(self, array, index, odd):
        if index == len(array) - 1:
            return index
        
        if (index, odd) not in list(Solution.next_memo.keys()):
            if odd:
                min_geq = 1e99
                next_index = -1

                for i in range(index + 1, len(array)):

                    if array[i] == array[index]:
                        next_index = i
                        break
                    if array[i] > array[index]:
                        if array[i] < min_geq:
                            min_geq = array[i]
                            next_index = i        
            else:
                max_leq = -1e99
                next_index = -1

                for i in range(index + 1, len(array)):
                    if array[i] == array[index]:
                        next_index = i
                        break
                    if array[i] < array[index]:
                        if array[i] > max_leq:
                            max_leq = array[i]
                            next_index = i
            Solution.next_memo[(index, odd)] = next_index

        return Solution.next_memo[(index, odd)]            
        
    
    def can_get_to_end(self, array, index, odd):
        
        if (index, odd) not in list(Solution.memo.keys()):            
            next_index = self.get_next_move(array, index, odd)
            
            if next_index == len(array) - 1:
                Solution.memo[(index, odd)] = 1
            elif next_index == -1:
                Solution.memo[(index, odd)] = 0
            else:
                Solution.memo[(index, odd)] = self.can_get_to_end(array, next_index, not odd)
        
        return Solution.memo[(index, odd)]
        
    
    def other(self, a):
        
        b = list(sorted(list(range(len(a))), key=lambda i: a[i]))
        c = list(sorted(list(range(len(a))), key=lambda i: -a[i]))
        
        
        odd_next = {}
        even_next = {}
        i = 1
        while i < len(b):
            j = i
            while j < len(b) - 1 and b[j] <= b[i - 1]:
                j += 1
            if b[j] > b[i - 1]:
                odd_next[b[i - 1]] = b[j]
            i += 1
        
        i = 1
        while i < len(c):
            j = i
            while j < len(c) - 1 and c[j] <= c[i - 1]:
                j += 1
            if c[j] > c[i - 1]:
                even_next[c[i - 1]] = c[j]
            i += 1
        
        
#         print(b)
#         print(c)
        
#         print(odd_next)
#         print(even_next)
        
        paths = 0
        
        for start in list(odd_next.keys()):
            
            index = start
            can_go = True
            odd = True
            while can_go and index != len(a) - 1:
                if odd:
                    if index in list(odd_next.keys()):
                        index = odd_next[index]
                    else:
                        can_go = False
                else:
                    if index in list(even_next.keys()):
                        index = even_next[index]
                    else:
                        can_go = False
                odd = not odd
            if index == len(a) - 1:
                # print(start)
                paths += 1

        if len(a) - 1 not in list(odd_next.keys()):
            paths += 1
        
        
        return paths
    
    
    def oddEvenJumps(self, a: List[int]) -> int:
        return self.other(a)
    
    
#         paths = 0
        
#         for i in range(len(a)):
#             _ = self.can_get_to_end(a, len(a) - i, True)
#             _ = self.can_get_to_end(a, len(a) - i, False)
        
#         for i in range(len(a)):
#             paths += self.can_get_to_end(a, i, True)
        
#         Solution.memo = {}
#         Solution.next_memo = {}
#         return paths

