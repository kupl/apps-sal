class Solution:
    def longestSubarray(self, array: List[int]) -> int:
        i = 0
        lenght = 0
        stack = deque()
        zero = False
        while i < len(array):
            if array[i] == 1:
                stack.append(array[i])
                i += 1
            else:
                if zero == False:
                    stack.append(array[i])
                    zero = True
                    i += 1
                else:
                    temp = len(stack) - 1
                    if temp > lenght:
                        lenght = temp
                    while stack[0] != 0:
                        stack.popleft()
                    stack.popleft()
                    zero = False
            if len(stack) > lenght:
                lenght = len(stack) - 1
        return (lenght)
