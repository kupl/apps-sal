class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        book = [1]*len(arr)
        index = collections.defaultdict(list)
        for i in range(len(arr)):
            index[arr[i]].append(i)
        val = list(index.keys())
        val.sort(reverse = True)
        for v in val:
            for i in index[v]:
                height = arr[i]
                for j in range(i+1, i+d+1):
                    if j == len(arr):
                        break
                    if arr[j] > height:
                        book[i] = max(book[i], book[j]+1)
                        height = arr[j]
                height = arr[i]
                for j in range(i-1, i-d-1, -1):
                    if j == -1:
                        break
                    if arr[j] > height:
                        book[i] = max(book[i], book[j]+1)
                        height = arr[j]
        return max(book)
