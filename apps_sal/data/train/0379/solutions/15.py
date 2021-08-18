class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.mod_value = pow(10, 9) + 7
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0
        format_nums1 = []
        format_nums2 = []
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                if len(format_nums1) == 0 or format_nums1[-1][1] == 0:
                    format_nums1.append([[0, 0], 1])
                if len(format_nums2) == 0 or format_nums2[-1][1] == 0:
                    format_nums2.append([[0, 0], 1])
                format_nums1.append([[0, nums1[i]], 0])
                format_nums2.append([[0, nums2[j]], 0])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                if len(format_nums1) == 0 or format_nums1[-1][1] == 0:
                    format_nums1.append([[0, nums1[i]], 1])
                else:
                    format_nums1[-1][0] = self.add_value(format_nums1[-1][0], nums1[i])
                i += 1
            else:
                if len(format_nums2) == 0 or format_nums2[-1][1] == 0:
                    format_nums2.append([[0, nums2[j]], 1])
                else:
                    format_nums2[-1][0] = self.add_value(format_nums2[-1][0], nums2[j])
                j += 1
        while i < n:
            if len(format_nums1) == 0 or format_nums1[-1][1] == 0:
                format_nums1.append([[0, nums1[i]], 1])
            else:
                format_nums1[-1][0] = self.add_value(format_nums1[-1][0], nums1[i])
            i += 1
        while j < m:
            if len(format_nums2) == 0 or format_nums2[-1][1] == 0:
                format_nums2.append([[0, nums2[j]], 1])
            else:
                format_nums2[-1][0] = self.add_value(format_nums2[-1][0], nums2[j])
            j += 1
        if format_nums1[-1][1] == 0:
            format_nums1.append([[0, 0], 1])
        if format_nums2[-1][1] == 0:
            format_nums2.append([[0, 0], 1])
        max_value1 = [0, 0]
        max_value2 = [0, 0]
        n = len(format_nums1)
        for i in range(n):
            if format_nums1[i][1] == 0 or i == 0:
                max_value1 = self.add_value_pair(max_value1, format_nums1[i][0])
                max_value2 = self.add_value_pair(max_value2, format_nums2[i][0])
            else:
                temp1 = self.add_value_pair(max_value2, format_nums1[i][0])
                temp2 = self.add_value_pair(max_value1, format_nums2[i][0])
                max_value1 = self.max(self.add_value_pair(max_value1, format_nums1[i][0]), temp1)
                max_value2 = self.max(self.add_value_pair(max_value2, format_nums2[i][0]), temp2)
        return self.max(max_value1, max_value2)[1]

    def add_value(self, value_pair, value):
        value_pair[1] += value
        while (value_pair[1] >= self.mod_value):
            value_pair[0] += 1
            value_pair[1] -= self.mod_value
        return value_pair

    def add_value_pair(self, value_pair1, value_pair2):
        result = [value_pair1[0] + value_pair2[0], value_pair1[1] + value_pair2[1]]
        while result[1] >= self.mod_value:
            result[0] += 1
            result[1] -= self.mod_value
        return result

    def max(self, value_pair1, value_pair2):
        if value_pair1[0] == value_pair2[0]:
            if (value_pair1[1] > value_pair2[1]):
                return value_pair1
        elif value_pair1[0] > value_pair2[0]:
            return value_pair1
        return value_pair2
