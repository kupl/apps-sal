class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        high = position[-1] - position[0]
        low = 1
        output = [0]
        k = [m]

        def check(distance):
            previous = -1
            m = k[-1]
            previous = position[0]
            m -= 1
            if m == 0:
                return True
            for i in range(1, len(position)):

                if position[i] - previous >= distance:
                    previous = position[i]
                    m -= 1
                    if m == 0:
                        break
            if m == 0:
                return True
            return False

        def binary(low, high):

            mid = (low + high) // 2

            if low > high:

                return
            if check(mid):

                output[0] = mid

                binary(mid + 1, high)
            else:
                binary(low, mid - 1)
        binary(low, high)
        return output[-1]
