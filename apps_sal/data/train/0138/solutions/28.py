class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] > 0 else 0
        p1 = p2 = 0
        answer = 0
        curr_len = 0
        neg_indx = deque([])
        while p2 < n:
            num = nums[p2]
            if num == 0:
                answer = max(answer, curr_len)
                curr_len = 0
                p2 += 1
                p1 = p2
                neg_indx = deque([])
            elif num > 0:
                curr_len += 1
                answer = max(answer, curr_len)
                p2 += 1
            else:
                neg_indx.append(p2)
                j = p2 + 1
                found = False
                while j < n:
                    num2 = nums[j]
                    if num2 <= 0:
                        if num2 < 0:
                            neg_indx.append(j)
                            found = True
                        break
                    j += 1
                if found:
                    curr_len += (j - p2 + 1)
                    answer = max(answer, curr_len)
                    if j == n - 1:
                        return answer
                    else:
                        p2 = j + 1
                else:
                    first_neg = neg_indx.popleft()
                    while p1 <= first_neg:
                        p1 += 1
                        curr_len -= 1
                    if p1 > p2:
                        p2 = p1
                        answer = max(answer, curr_len)
                        curr_len = 0
                    else:
                        curr_len += 1
                        p2 += 1
                    continue
        return answer


#[1, -4, 3, 2, 0, 2, -2, 3, -2, -2, 3, 4, 5]
