class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        # stack=[]
        # cnt_stack=[]
        # for char in s:
        #     if not stack or stack[-1] !=char:
        #         stack.append(char)
        #         cnt_stack.append(1)
        #     else:
        #         cnt_stack[-1] +=1
        #     if cnt_stack[-1] == k:
        #         cnt_stack.pop()
        #         stack.pop()
        # return ''.join([stack[i]*cnt_stack[i] for i in range(len(stack))])
        stack = [[0, '#']]
        for char in s:
            if char == stack[-1][1]:
                stack[-1][0] += 1
                if stack[-1][0] == k:
                    stack.pop()
            else:
                stack.append([1, char])
        return ''.join(c * k for c, k in stack)
