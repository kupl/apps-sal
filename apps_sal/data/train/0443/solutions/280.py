class Solution:
    def numTeams(self, a: List[int]) -> int:
        list1 = []
        for i in range(len(a) - 2):
            for j in range(i + 1, len(a) - 1):
                for k in range(j + 1, len(a)):
                    if a[i] < a[j] < a[k]:
                        list1.append((a[i], a[j], a[k]))
                    if a[i] > a[j] > a[k]:
                        list1.append((a[i], a[j], a[k]))
        return len(list1)
