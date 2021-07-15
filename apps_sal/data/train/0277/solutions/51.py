class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        light = sorted([(light[i], i) for i in range(len(light))], key=lambda t: t[0])
        go_over = list([t[1] for t in light])
                     
        smallest_distance_left_until_blue = 0
        count = 0
        for i in range(len(go_over)):
            smallest_distance_left_until_blue = max(smallest_distance_left_until_blue - 1, 0, go_over[i] - i)
            if smallest_distance_left_until_blue == 0:
                count += 1
            
        return count

