class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxs = max(arr)
        if k > arr.index(maxs):
            return maxs
        dic = {}

        ind = arr.index(maxs)

        i = 0
        seen = set()
        while i < ind + 1:
            maxs = max(arr[0], arr[1])
            mins = min(arr[0], arr[1])
            arr[0], arr[1] = mins, maxs
            if maxs not in dic:
                dic[maxs] = 1
            else:
                dic[maxs] += 1
            arr.append(arr.pop(0))
            if dic[maxs] == k:
                return maxs
            seen.add(dic[maxs])
            if k in seen:
                break
            i += 1

        lst = [k for k, v in list(dic.items()) if v == k]
        if lst:
            return lst[0]
        else:
            return max(arr)
