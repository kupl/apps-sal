class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_array = [abs(a - b) for (a, b) in zip(list(map(ord, s)), list(map(ord, t)))]
        left = right = t = mx = 0
        while right < len(cost_array):
            t += cost_array[right]
            if t > maxCost:
                t -= cost_array[left]
                left += 1
            right += 1
            mx = max(mx, right - left)
        return mx
