class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating) - 2):
            for j in range(i, len(rating) - 1):
                for k in range(j, len(rating)):
                    if rating[i] > rating[j] > rating[k]:
                        result += 1
                    if rating[i] < rating[j] < rating[k]:
                        result += 1
        return result


#         up_list = []
#         down_list = []
#         result = 0
#         for i in range(len(rating)):
#             up_list.append([i])
#             down_list.append([i])
#             for sub_list in up_list:
#                 if len(sub_list) == 1 and sub_list[0] < rating[i]:
#                     new_list = sub_list + [rating[i]]
#                     up_list.append(new_list)
#                 elif len(sub_list) == 2 and sub_list[-1] < rating[i]:
#                     up_list.append([sub_list[0], rating[i]])
#                     up_list.append([sub_list[1], rating[i]])
#                     result += 1
#                 elif len(sub_list) == 2 and sub_list[0] < rating[i]:
#                     up_list.append([sub_list[0], rating[i]])
#                     up_list.append([rating[i], sub_list[1]])

#             for sub_list in down_list:
#                 if len(down_list) == 1 and down_list[0] > rating[i]:
#                     new_list = sub_list + [rating[i]]
#                     down_list.append(new_list)
#                 elif len(sub_list) == 2 and sub_list[-1] > rating[i]:
#                     down_list.append([sub_list[0], rating[i]])
#                     down_list.append([sub_list[1], rating[i]])
#                     result += 1
#                 elif len(sub_list) == 2 and sub_list[0] > rating[i]:
#                     down_list.append([sub_list[0], rating[i]])
#                     down_list.append([rating[i], sub_list[1]])
#         return result
