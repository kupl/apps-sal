class Solution:
    def maxRepOpt1(self, text: str) -> int:
        lst, lookup = list(), dict()
        ptr = 0
        while ptr < len(text):
            curr, count = text[ptr], 0
            while ptr < len(text) and curr == text[ptr]:
                count += 1
                ptr += 1
            lookup[curr] = lookup.get(curr, 0) + count
            lst.append((curr, count))
        res = 0
        for i in range(len(lst)):
            if 0 < i < len(lst)-1:
                if lst[i-1][0] == lst[i+1][0] and lst[i][1] == 1:
                    curlen = lst[i-1][1]+lst[i+1][1]
                    if lookup[lst[i-1][0]] > curlen:
                        curlen += 1
                    res = max(res, curlen)
                    continue
            curlen = lst[i][1]
            if lookup[lst[i][0]] > curlen:
                curlen += 1
            res = max(res, curlen)
        return res
