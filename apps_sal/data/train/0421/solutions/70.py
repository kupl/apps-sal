def analize(arr):
    curstr = 1
    streaks = {}
    strstart = arr[0]
    for ii, val in enumerate(arr[:-1]):
        if arr[ii] == arr[ii + 1] - 1:
            curstr += 1
        else:
            streaks[strstart] = curstr
            strstart = arr[ii + 1]
            curstr = 1
    streaks[strstart] = curstr
    maxstr = max(streaks.values())
    return([(ii, maxstr) for ii in streaks if streaks[ii] == maxstr])


class Solution:
    def lastSubstring(self, s: str) -> str:
        index = {}
        for char in set(s):
            index[char] = [ic for ic, cc in enumerate(s) if cc == char]
#        print(index)
#        return 'a'
        maxchar = max(index.keys())
        front = analize(index[maxchar])
        curbest = ''
#        print(front,len(s))
        while front != []:
            curbest = curbest + s[front[0][0]] * front[0][1]
            nxt = [s[u[0] + u[1]] for u in front if u[0] + u[1] < len(s)]
#            print(front,curbest,nxt)
#            return 'a'
            if nxt != []:
                maxnxt = max(nxt)
                front = [(u[0] + u[1], 1) for u in front if u[0] + u[1] < len(s) and s[u[0] + u[1]] == maxnxt]
            else:
                front = []
        return curbest
