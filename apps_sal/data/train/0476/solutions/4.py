class Solution:
    def check(self, target, p1, s1, p2, s2):
        if p1 == target and p2 == target:
            return True
        if p1 == target or p2 == target:
            return False
        d1 = float(target - p1)
        d2 = float(target - p2)
        if d1 / float(s1) <= d2 / float(s2):
            return True
        return False

    def solve(self, target, pos, speed):
        arr = []
        for i in range(len(pos)):
            p = pos[i]
            s = speed[i]
            arr.append((p, s))
        arr = sorted(arr)
        counter = 0
        ln = len(arr)
        i = ln - 1
        # print(arr)
        while i >= 0:
            p2, s2 = arr[i]
            counter += 1
            j = i - 1
            while j >= 0:
                p1, s1 = arr[j]
                if not self.check(target, p1, s1, p2, s2):
                    # print('not checked:', target, (p1, s1), (p2, s2))
                    break
                j -= 1
            i = j
        return counter

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return self.solve(target, position, speed)
