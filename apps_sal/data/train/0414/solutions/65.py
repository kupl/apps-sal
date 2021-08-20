class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        check = {}
        num_0 = arr[0]
        num_1 = arr[1]
        num_wins = 0
        if len(arr) == 2:
            return max(arr[0], arr[1])
        if len(arr) < k:
            arr.sort(reverse=True)
            return arr[0]
        while num_wins < k and num_1 not in list(check.keys()):
            if num_0 > num_1:
                arr.remove(num_1)
                arr.append(num_1)
                check[num_1] = num_1
                num_1 = arr[1]
                num_wins += 1
            else:
                arr.remove(num_0)
                arr.append(num_0)
                check[num_0] = num_0
                num_0 = arr[0]
                num_1 = arr[1]
                num_wins = 1
        return num_0
