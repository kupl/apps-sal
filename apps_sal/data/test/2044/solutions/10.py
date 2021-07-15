N, M = map(int, input().split())
curname = 0

arr = map(int, input().split())
for a in arr:
    curname += a
    cnt = curname // M
    curname = curname % M
    print(cnt, end=' ')
    



