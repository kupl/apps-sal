class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for i, r in enumerate(ranges):
            if r > 0:
                taps.append([max(0, i - r), -min(n, i + r)])
        if not taps:
            return -1
        taps.sort()
        if taps[0][0] != 0:
            return -1
        stack = [[taps[0][0], abs(taps[0][1])]]
        
        #print(taps)

        for t in taps[1:]:
            if stack[-1][1] == n:
                break
            l, r = t[0], abs(t[1])
            if r <= stack[-1][1]:
                continue
            if l > stack[-1][1]:
                return - 1
            if len(stack) == 1:
                stack.append([l, r])
            else:    
                if l <= stack[-2][1]:
                    stack.pop()
                stack.append([l, r])

        #print(stack)
        return len(stack)

