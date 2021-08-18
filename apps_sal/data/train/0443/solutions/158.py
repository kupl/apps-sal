class Solution:

    def three(self, three, final):

        if three == True:
            print(final)

    def numTeams(self, rating: List[int]) -> int:

        i = 0
        j = 0
        k = 0

        final = []

        three = None
        count = 0
        while i < len(rating):
            j = i + 1
            while j < len(rating):
                k = j + 1
                while k < len(rating):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        count += 1
                    k += 1
                j += 1
            i += 1
        return count

    def numTeams_praj(self, rating: List[int]) -> int:

        i = 0
        final = []

        three = None
        count = 0
        while i < len(rating):
            final.append(rating[i])
            j = i + 1
            while j < len(rating):
                final.append(rating[j])
                if rating[j] > rating[i]:
                    new = rating[j + 1:]
                    for ele in new:
                        if ele > rating[j]:
                            final.append(ele)
                            three = True

                            self.three(three, final)
                            count += 1
                            final = []
                            final.append(rating[i])
                            final.append(rating[j])

                        else:
                            three = False
                            rating[j] = ele

                j += 1
            i += 1
        return count
