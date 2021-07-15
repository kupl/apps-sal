N = int(input())
A = list(map(int,input().split()))

s = ans1 = 0
for i,a in enumerate(A):
    s += a
    if i%2:
        if s <= 1:
            ans1 += 1-s
            s = 1
    else:
        if s >= -1:
            ans1 += s+1
            s = -1

s = ans2 = 0
for i,a in enumerate(A):
    s += a
    if i%2==0:
        if s <= 1:
            ans2 += 1-s
            s = 1
    else:
        if s >= -1:
            ans2 += s+1
            s = -1

print(min(ans1,ans2))
