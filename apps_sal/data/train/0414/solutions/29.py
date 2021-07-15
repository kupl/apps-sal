class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        
        stack = [arr[0]]
        cnt = 0
        for n in arr[1:]:
            if cnt == k:
                return stack[0]
            if n < stack[-1]:
                cnt += 1
            else:
                stack.pop()
                stack.append(n)
                cnt = 1
        
        return stack[0]

