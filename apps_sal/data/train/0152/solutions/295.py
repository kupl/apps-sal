class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check_force(position, pivot, m):
            anchor = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - anchor >= pivot:
                    anchor = position[i]
                    cnt += 1

                    if cnt == m:
                        # print(\"Successfully placed all baskets\")
                        return True
            return False

        position = sorted(position)
        low, high = 0, position[-1]
        output = -1

        # Standard binary search recipe
        while low < high:
            pivot = (low + high) // 2
            if check_force(position, pivot, m):
                output = max(output, pivot)
                low = pivot + 1
            else:
                high = pivot
        return output
