class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        if n % 2 == 1:
            i = 0
            mid = (2*(int(n/2)))+1
            # print(mid)
            # print(int(n/2))
            while i < int(n/2):
                # print(i)
                count += mid-((2*i)+1)
                i+=1
        else:
            i = 0
#             [1, 3, 5, 7, 9, 11]
            mid = (2*((n/2)))
            # print(mid)
            while i < n/2-1:
                # print(i)
                # print(count)
                count += mid-((2*i)+1)
                i +=1
            count += 1
        return int(count)
    

