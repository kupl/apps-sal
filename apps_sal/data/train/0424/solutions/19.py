class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A)
        shifts = [ii for ii in range(size)]
        max_overlap = 0
        for x in shifts:
            for y in shifts:
                max_overlap = max(self.shift_and_count(x_shift=x, y_shift=y, array_reference=A, array_to_be_shifted=B), max_overlap)
                max_overlap = max(self.shift_and_count(x_shift=x, y_shift=y, array_reference=B, array_to_be_shifted=A), max_overlap)
        return max_overlap

    def shift_and_count(self, x_shift: int, y_shift: int, array_reference: List[List[int]], array_to_be_shifted: List[List[int]]) -> int:
        if x_shift > 0:
            array_to_be_shifted = self.shift_left(array=array_to_be_shifted, shifts=x_shift)
        if y_shift > 0:
            array_to_be_shifted = self.shift_up(array=array_to_be_shifted, shifts=y_shift)
        return self.overlap(array_a=array_reference, array_b=array_to_be_shifted)

    def overlap(self, array_a: List[List[int]], array_b: List[List[int]], value: int = 1) -> int:
        common_values = 0
        for (row_a, row_b) in zip(array_a, array_b):
            for (a, b) in zip(row_a, row_b):
                if a == b == value:
                    common_values += 1
        return common_values

    def shift_up(self, array: List[List[int]], shifts: int, fill_value: int = 0) -> List[List[int]]:
        a = array[shifts:]
        for _ in range(shifts):
            a.append([fill_value] * len(array[0]))
        return a

    def shift_left(self, array: List[List[int]], shifts: int, fill_value: int = 0) -> List[List[int]]:
        a = []
        for sublist in array:
            last_elements = [fill_value] * shifts
            sublist = sublist[shifts:] + last_elements
            a.append(sublist)
        return a
