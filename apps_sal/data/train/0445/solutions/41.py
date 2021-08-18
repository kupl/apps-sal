
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        l = len(nums)

        biggest = nums[:min(4, l)]
        smallest = nums[:min(4, l)]
        for i in range(4, l):
            num = nums[i]
            biggest.append(num)
            smallest.append(num)

            biggest.remove(min(biggest))
            smallest.remove(max(smallest))

        if len(biggest) < 4:
            return 0

        bfs = [(sorted(biggest), sorted(smallest), 0)]

        opt = max(biggest) - min(smallest)
        while bfs:
            new_biggest, new_smallest, changes = bfs.pop(0)

            if changes == 3:
                opt = min(
                    opt,
                    max(new_biggest) - min(new_smallest)
                )
                continue

            bfs.append((new_biggest[:-1], list(new_smallest), changes + 1))
            bfs.append((list(new_biggest), new_smallest[1:], changes + 1))

        return opt
