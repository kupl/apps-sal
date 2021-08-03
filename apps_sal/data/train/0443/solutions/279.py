class Solution:
    def numTeams(self, rating: List[int]) -> int:
        stack = []
        list1 = []
        n = len(rating)
        for i in range(0, n - 2):
            # check 3 items from in the list iterating using i,j,k.i until n-2,j until n-1 and k untill n
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        stack.append(rating[i])
                        stack.append(rating[j])
                        stack.append(rating[k])
                        # print(\"stack\",stack)
                        list1.append(stack)
                    stack = []
        # print(list1)
        return len(list1)
