from collections import defaultdict

h,w,n = map(int,input().split())

d = defaultdict(int)

for _ in range(n):
    a,b = map(int,input().split())

    for i in range(-1,2):
        for j in range(-1,2):
            if 1 < a+i < h and 1 < b+j < w:
                d[(a+i,b+j)] += 1

ans = [0]*10

for i in d.values():
    ans[i] += 1

ans[0] = (h-2)*(w-2)-sum(ans)
for i in ans:
    print(i)
