class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt = 0
        max_el = 0

        for element in arr:
            if element > max_el:
                max_el = element

        if(k >= len(arr) - 1):
            return max_el

        while(cnt < k):
            if(arr[0] > arr[1]):
                arr.append(arr[1])
                arr.remove(arr[1])
                cnt += 1
            else:
                arr.append(arr[0])
                arr.remove(arr[0])
                cnt = 1

        return arr[0]
