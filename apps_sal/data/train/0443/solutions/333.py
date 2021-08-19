class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating) - 2):
            head = rating[i]
            # print(head)
            for j in range(len(rating) - i - 2):
                sec = rating[i + j + 1]
                # print(head,sec)
                if sec > head:
                    for k in rating[i + j + 2::]:
                        if k > sec:
                            ans = ans + 1
                elif sec < head:
                    for k in rating[i + j + 2::]:
                        if k < sec:
                            ans = ans + 1
        return ans
