class Solution:
    def racecar(self, target: int) -> int:
        barrier = 2 * target
        heap = [[0, 0, 1]]
        seen = set()
        while heap:
            step, position, speed = heappop(heap)

            if position == target:
                return step - 1

            if (position, speed) in seen:
                continue
            seen.add((position, speed))

            k = 0
            while True:
                new_pos = position + speed * (2 ** k - 1)

                if -barrier <= new_pos <= barrier:
                    heappush(heap, [step + k + 1, new_pos, -speed])
                else:
                    break
                k += 1
