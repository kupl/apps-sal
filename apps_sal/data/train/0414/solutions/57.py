class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        timeswon = 0
        if arr.index(max_num) < k:
            print(1)
            return max_num
        while timeswon < k:
            if arr[0] == max_num:
                print(2)
                break
            if arr[0] > arr[1]:
                print(3)
                arr.append(arr[1])
                del arr[1]
                timeswon += 1
            else:
                print(4)
                arr.append(arr[0])
                del arr[0]
                timeswon = 1
        return arr[0]
