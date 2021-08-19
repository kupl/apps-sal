class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        array_length = len(arr)
        if k > array_length:
            return max(arr)
        index_one = 0
        index_two = 1
        wins = 0
        while index_two < array_length:
            if index_one == index_two:
                index_two += 1
                if index_two == array_length:
                    break
            if arr[index_one] > arr[index_two]:
                wins += 1
                if wins == k:
                    return arr[index_one]
                index_two += 1
                continue
            index_one += 1
            index_two = index_one - 1
            wins = 0
        return max(arr)
