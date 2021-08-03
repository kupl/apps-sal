class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ln = len(arr)

        #win = arr[0]
        cnt = -1
        idx = 0

        if k >= ln:
            return max(arr)

        while True:
            idx = 0
            arr2 = []

            # print(arr)

            for i in range(1, ln):
                if arr[idx] > arr[i]:
                    cnt += 1
                    arr2.append(arr[i])
                else:
                    arr2.append(arr[idx])
                    idx = i
                    cnt = 1

                if cnt >= k:
                    return arr[idx]

            arr = [arr[idx]] + arr2
            # print(arr2)

        return 0
        pass
