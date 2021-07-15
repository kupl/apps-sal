class Solution:
    def numTeams(self, rating: List[int]) -> int:
        possibleTeams = []
        temp = []
        for i in range(len(rating)):
            soldier_i = rating[i]
            for j in range(i+1, len(rating)):
                soldier_j = rating[j]
                if soldier_j > soldier_i:
                    increasing = True
                else:
                    increasing = False
                for k in range(j+1, len(rating)):
                    soldier_k = rating[k]
                    if increasing and soldier_k > soldier_j:
                        possibleTeams.append((soldier_i, soldier_j, soldier_k))
                    if increasing == False and soldier_k < soldier_j:
                        possibleTeams.append((soldier_k, soldier_j, soldier_i))
        return len(possibleTeams)

