class Solution:
    def numTeams(self, a: List[int]) -> int:
        count = 0
        for i in range(len(a) - 2):
            for j in range(i + 1, len(a) - 1):
                for k in range(j + 1, len(a)):
                    if a[i] < a[j] < a[k]:
                        count += 1
                    if a[i] > a[j] > a[k]:
                        count += 1
        return count
