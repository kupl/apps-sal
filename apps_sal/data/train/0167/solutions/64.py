class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int:
        building = [[0] * (eggs + 1) for _ in range(floors + 1)]
        currFloor = 0

        while building[currFloor][eggs] < floors:
            currFloor += 1
            for i in range(1, eggs + 1):
                building[currFloor][i] = building[currFloor - 1][i - 1] + building[currFloor - 1][i] + 1

        return currFloor
