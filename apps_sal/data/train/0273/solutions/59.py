class Solution:
    def racecar(self, target: int) -> int:
        max_step = int(log(target,2)) + 2
        barrier = 2 * target + 2
        heap = [[i + 1, 0 + (2 ** i - 1), -1] for i in range(max_step+1)]
        seen = {}
        while heap:
            step, position, speed = heappop(heap)
            
            if position == target:
                return step - 1
            
            if (position,speed) in seen and seen[position,speed] <= step:
                continue
            seen[position,speed] = step

            k = 0
            while True:
                new_pos = position + speed * (2 ** k - 1)

                if -barrier <= new_pos <= barrier:
                    heappush(heap, [step + k + 1, new_pos, -speed])
                else:
                    break
                    
                k += 1

