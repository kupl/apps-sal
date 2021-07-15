class Solution:
    def numTeams(self, rating: List[int]) -> int:
        track = []
        res = 0
        def backtrack(increase, index):
            nonlocal res
            if len(track) == 3:
                
                res +=1
                return
            for i in range(index, len(rating)):
                if index == 0:
                    track.append(rating[i])
                    backtrack(increase, i+1)
                    track.pop()
                else:
                    if increase:
                        if rating[i] > track[-1]:
                            track.append(rating[i])
                            backtrack(True, i+1)
                            track.pop()
                    if not increase:
                        if rating[i] < track[-1]:
                            track.append(rating[i])
                            backtrack(False, i+1)
                            track.pop()
        backtrack(True, 0)
        backtrack(False, 0)
        return res

