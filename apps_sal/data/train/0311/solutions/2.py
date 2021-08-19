class Solution:

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        current_min = 1
        current_max = 1
        desc_len = 1
        cnt = 1
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i - 1]:
                if current_min == 1:
                    cnt += desc_len
                    if desc_len < current_max:
                        cnt -= 1
                else:
                    current_max = current_min
                    current_min = 1
                desc_len += 1
            elif ratings[i] > ratings[i - 1]:
                current_min += 1
                current_max = current_min
                cnt += current_min - 1
                desc_len = 1
            else:
                current_min = 1
                current_max = 1
                desc_len = 1
            cnt += 1
        return cnt
