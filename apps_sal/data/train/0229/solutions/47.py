class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        def update_map(count, small, large):
            small_count = count[small]
            large_count = count[large]
            min_count = min(small_count, large_count)
            
            count[small] += -min_count
            if small != large:
                count[large] += -min_count
            
        if not A:
            return True
        element_count = {}
        ordered_elements = list(set(A))
        ordered_elements.sort()
        
        for number in A:
            if number not in element_count:
                element_count[number] = 0
            element_count[number] += 1
        
        for number in ordered_elements:
            number_count = element_count[number]
            double_number = number * 2
            if double_number in element_count:
                update_map(element_count, number, double_number)
            
        for number in element_count:
            if element_count[number] != 0:
                return False
        return True
                    
                

