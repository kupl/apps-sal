class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0
        counts = [0] * (limit + 1)
        for person_weight in people:
            counts[person_weight] += 1
        
        start = 0
        end = len(counts) - 1
        while start <= end:
            while start <= end and counts[start] <= 0:
                start += 1
            while start <= end and counts[end] <= 0:
                end -= 1
            if start > end:
                break
            if start + end <= limit:
                counts[start] -= 1
            counts[end] -= 1
            num_boats += 1
        return num_boats
