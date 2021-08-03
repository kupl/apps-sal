class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i, x in enumerate(rating):
            for j, y in enumerate(rating[i + 1:], i + 1):
                if y > x:
                    #print(f'i: {i}, j: {j}')
                    cnt += sum(z > y for z in rating[j + 1:])
                if y < x:
                    #print(f'i: {i}, j: {j}')
                    cnt += sum(z < y for z in rating[j + 1:])
        return cnt
