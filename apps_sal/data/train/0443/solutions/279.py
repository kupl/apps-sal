class Solution:

    def numTeams(self, rating: List[int]) -> int:
        stack = []
        list1 = []
        n = len(rating)
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        stack.append(rating[i])
                        stack.append(rating[j])
                        stack.append(rating[k])
                        list1.append(stack)
                    stack = []
        return len(list1)
