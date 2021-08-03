class Solution:
    def numTeams(self, rating: List[int]) -> int:

        i = 0
        final = []
        add = 0
        while i < len(rating):

            j = len(rating) - 1
            while j > i + 1:
                # print(rating[i],rating[j])
                k = j - 1
                while k > i:
                    # print(rating[i],rating[k],rating[j])
                    if rating[i] < rating[k] and rating[k] < rating[j]:
                        add += 1
                    if rating[i] > rating[k] and rating[k] > rating[j]:
                        add += 1
                    k -= 1

                j -= 1
            i += 1
        return add
#             j=i+1
#             k=len(rating)-1

#             while j<k:
#                 print(rating[i],rating[j],rating[k])

#                 if rating[i]<rating[j] and rating[j]<rating[k]:
#                     final.append((rating[i],rating[j],rating[k]))

#                 elif rating[i]>rating[j] and rating[j]>rating[k]:
#                     final.append((rating[i],rating[j],rating[k]))

#                 j+=1

#                 print(rating[i],rating[j],rating[k])
#                 print()
#             i+=1
#         print(final)
