class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = start + (end - start)//2
            print(mid)
            counter = 0
            summation = 0
            for i in weights:
                if summation+i==mid:
                    counter += 1
                    summation = 0
                elif summation+i>mid:
                    counter+= 1
                    summation = i
                elif summation<mid:
                    summation += i
            counter += 1
            print(counter)
            if counter >D: start = mid+1
            else: end = mid
        return start
