n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
a = sorted(a)
p = 0
cnt = 0
for i in a:
    while i - cnt > 0:
        print(i - cnt)
        cnt += i - cnt
        p += 1
        if p >= k:
            return
else:
    while p!=k:
        print(0)
        p += 1

