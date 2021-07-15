class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt = Counter()
        for i in range((len(arr))):
            if cnt[arr[0]] == k:
                break
            if arr[0] > arr[1]:
                arr.append(arr.pop(1))
                cnt[arr[0]]+=1
            elif arr[0] < arr[1]:
                arr.append(arr.pop(0))
                cnt[arr[0]]+=1
        return arr[0]
