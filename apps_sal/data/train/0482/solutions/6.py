class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        concept:
            we can do greedy: every time select the two nodes with smallest product as two leafs 
            why greedy works?
            
            we can also maintain a monotone decreasing stack
        '''
        stack = [arr[0]]
        _sum = 0
        for n in arr[1:]:
            while stack and n > stack[-1]:
                n1 = stack.pop()
                
                n2 = n if not stack or n < stack[-1] else stack[-1]
                # print(n1, n2)
                _sum += n1*n2
            stack.append(n)
        # print(stack)
        # print(_sum)
        while len(stack) > 1:
            n1 = stack.pop()
            n2 = stack.pop()
            _sum += n1*n2
            if not stack:
                break
            stack.append(max(n1, n2))
        return _sum

