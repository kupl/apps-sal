class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dict1 = {}
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] in dict1:
                dict1[arr[i]].append(i)
            else:
                dict1[arr[i]] = [i]
            cur = arr[i]
            j = 1
            while i + j < n:
                if arr[i + j] == cur:
                    j += 1
                else:
                    break
            if j > 1:
                dict1[arr[i]].append(i + j - 1)
            i += j

        curPoss = {0}
        cnt = 0
        while curPoss != []:
            nextPoss = set()
            for cur in curPoss:
                if cur == n - 1:
                    return cnt
                l = cur - 1
                if 0 < l < n and l not in curPoss and arr[l] != None:
                    nextPoss.add(l)
                r = cur + 1
                if 0 < r < n and r not in curPoss and arr[r] != None:
                    nextPoss.add(r)
                for i in dict1[arr[cur]]:
                    if i != cur and i not in curPoss and arr[i] != None:
                        nextPoss.add(i)
                arr[cur] = None
            curPoss = nextPoss
            cnt += 1
