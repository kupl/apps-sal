class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        def get_max_gap(array):
            array.sort()
            max_hor_width = array[0]
            for previous_cut, next_cut in zip(array, array[1:]):  
                max_hor_width = max(max_hor_width, next_cut - previous_cut)
                
            return max_hor_width

        return (get_max_gap(horizontalCuts) * get_max_gap(verticalCuts)) % 1000000007
    
# time complexity - nlogn - mainly sorting
# sub1: corner case for 0, n index
# sub2: result should be module
#  does insertion take extra time? - maybe just O(n) - could be avoided with smart comparison

