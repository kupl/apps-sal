class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        residual_list = arr
        filled_list = []
        winner_dict = {}
        residual_dict = []
        if k >= len(arr):
            return max(arr)
        for item in residual_list:
            filled_list.append(item)
            if len(filled_list) >= 2:
                l1 = filled_list[0]
                l2 = filled_list[1]
                winner = max(l1, l2)
                if winner in winner_dict:
                    winner_dict[winner] += 1
                else:
                    winner_dict[winner] = 1
                if winner_dict[winner] == k:
                    return winner
                filled_list.remove(min(l1, l2))
                residual_list.append(min(l1, l2))
            else:
                continue
