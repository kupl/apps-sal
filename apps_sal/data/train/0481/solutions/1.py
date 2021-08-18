class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Solution: Sort the list then use three pointers (i, j, k) to find the sum of 3 values that is closest to target.
        Store the current closest value and the distance from target.
        Current closest value can be compared using abs(target - value) and comparing to the stored distance from target.
        """
        arr, i, closest, dist = nums, 0, None, None
        arr.sort()

        if len(arr) == 3:
            return arr[0] + arr[1] + arr[2]

        while i < len(arr) - 2:
            if i > 0 and arr[i] > target:
                return closest
            if i == 0 or arr[i] != arr[i - 1]:
                j, k = i + 1, len(arr) - 1
                while j < k:
                    val = arr[i] + arr[j] + arr[k]
                    if val == target:
                        return val
                    temp_dist = abs(target - val)
                    if dist == None or temp_dist < dist:
                        closest = val
                        dist = temp_dist
                    if val < target:
                        j += 1
                    else:
                        k -= 1

            i += 1
        return closest
