class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        seen = set()
        stack = []
        start = 0
        for index, element in enumerate(popped):
            while element not in seen:
                stack.append(pushed[start]   )
                seen.add(pushed[start])
                start += 1
            catch = False
            while catch == False:
                if catch == False and len(stack) == 0:
                    return False
                e = stack.pop()
                if e == element:
                    catch = True
                        
        return True
        
        
        # 1 2   
        
        
        # #given one element
        #     not seen: keep push until we see
        #     seen: keep pop until we seen
                

