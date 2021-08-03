class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        #         start=0
        #         end=len(people)-1
        #         count=0
        #         #people=sorted(people)
        #         while start<=end:
        #             if people[start]+people[end]<=limit:
        #                 start+=1

        #             end-=1
        #          count+=1
        bucket = [0] * (limit + 1)
        for i in people:
            bucket[i] += 1
        start = 0
        end = len(bucket) - 1
        count = 0
        while start <= end:

            while start <= end and bucket[start] <= 0:
                start += 1

            while start <= end and bucket[end] <= 0:
                end -= 1

            if bucket[start] <= 0 and bucket[end] <= 0:
                break

            count += 1
            if start + end <= limit:
                bucket[start] -= 1

            bucket[end] -= 1

        return count
