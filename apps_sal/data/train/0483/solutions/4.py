class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = (len(height) - 1) * min([height[0], height[-1]])
        left_idx = 0
        right_idx = len(height) - 1
        while left_idx < right_idx:
            if height[left_idx] < height[right_idx]:
                start = left_idx + 1
                while start < right_idx:
                    if height[start] > height[left_idx]:
                        left_idx = start
                        area2 = (right_idx - left_idx) * min([height[left_idx], height[right_idx]])
                        if area2 > area:
                            area = area2
                        break
                    start += 1
                if start != left_idx:
                    break
            elif height[left_idx] > height[right_idx]:
                start = right_idx - 1
                while start > left_idx:
                    if height[start] > height[right_idx]:
                        right_idx = start
                        area2 = (right_idx - left_idx) * min([height[left_idx], height[right_idx]])
                        if area2 > area:
                            area = area2
                        break
                    start -= 1
                if start != right_idx:
                    break
            else:
                left_idx += 1
        return area
