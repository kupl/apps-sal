class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr): return max(arr)
        winner=arr[0]
        c=collections.Counter()
        for i in arr[1:]:
            winner=max(winner,i)
            c[winner]+=1
            if c[winner]==k: return winner
        return winner
