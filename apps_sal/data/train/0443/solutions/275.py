class Solution:
    def numTeams(self, rating: List[int]) -> int:
        possible_list = []
        count = 0
        for i, first_num in enumerate(rating[:-2]):
            for j, sec_num in enumerate(rating[i + 1:-1]):
                for k, third_num in enumerate(rating[j + i + 2:]):
                    possible_list.append((first_num, sec_num, third_num))
        for pair in possible_list:
            if pair[0] > pair[1] > pair[2] or pair[2] > pair[1] > pair[0]:
                count += 1
        return count
