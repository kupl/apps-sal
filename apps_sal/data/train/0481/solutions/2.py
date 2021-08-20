class Solution:

    def threeSumClosest(self, array, target):
        """ Returns sum of integers from array closest to target.
        Time complexity: O(n ^ 2). Space complexity: O(n),
        where n is len(array).
        """
        array.sort()
        n = len(array)
        best_sum = float('inf')
        for i in range(n - 2):
            if i > 0 and array[i] == array[i - 1]:
                continue
            diff = target - array[i]
            (x, y) = (i + 1, n - 1)
            best_diff = float('inf')
            while x < y:
                curr_diff = array[x] + array[y]
                if curr_diff == diff:
                    return target
                elif curr_diff < diff:
                    x += 1
                else:
                    y -= 1
                if abs(curr_diff - diff) < abs(best_diff - diff):
                    best_diff = curr_diff
            curr_sum = array[i] + best_diff
            if abs(curr_sum - target) < abs(best_sum - target):
                best_sum = curr_sum
        return best_sum
