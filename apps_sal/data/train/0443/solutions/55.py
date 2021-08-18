class Solution:
    def numTeams(self, rating: List[int]) -> int:

        elm_less_than_cur_to_left, elm_less_than_cur_to_right, elm_greater_than_cur_to_left, elm_greater_than_cur_to_right = [0] * len(rating), [0] * len(rating), [0] * len(rating), [0] * len(rating)

        i = 0
        res = 0

        while i < len(rating):
            k = i - 1
            while k >= 0:
                if rating[i] > rating[k]:
                    elm_less_than_cur_to_left[i] += 1

                elif rating[i] < rating[k]:
                    elm_greater_than_cur_to_left[i] += 1
                k -= 1

            k = i + 1
            while k < len(rating):
                if rating[i] > rating[k]:
                    elm_less_than_cur_to_right[i] += 1

                elif rating[i] < rating[k]:
                    elm_greater_than_cur_to_right[i] += 1
                k += 1

            i += 1
        for i in range(0, len(rating)):
            res += (elm_less_than_cur_to_left[i] * elm_greater_than_cur_to_right[i]) + (elm_less_than_cur_to_right[i] * elm_greater_than_cur_to_left[i])

        return res
