class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        a = arr[0]
        b = arr[1]
        winner = a if a > b else b
        winning_count = 1
        for current_candidate_index in range(2, len(arr)):
            if winning_count >= k:
                break
            if winner > arr[current_candidate_index]:
                winning_count += 1
            else:
                winner = arr[current_candidate_index]
                winning_count = 1
        return winner
