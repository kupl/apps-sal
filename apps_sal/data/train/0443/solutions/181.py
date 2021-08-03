class Solution:
    def numTeams(self, a: List[int]) -> int:
        output = 0
        for i in range(len(a[:-2])):
            for j in range(len(a[:-1])):
                if a[j] > a[i] and j > i:
                    for k in range(len(a)):
                        if a[k] > a[j] and k > j:
                            output += 1
                elif a[j] < a[i] and j > i:
                    for k in range(len(a)):
                        if a[k] < a[j] and k > j:
                            output += 1
        return output
