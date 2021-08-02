from bisect import bisect_right

n = int(input())
a = [-int(input()) for _ in range(n)]

li = list()
for e in a:
    i = bisect_right(li, e)
    if i == len(li):
        li.append(e)
    else:
        li[i] = e

ans = len(li)
print(ans)
