N = int(input())
A = [int(input()) for _ in range(N)]

m,s = 0,0
for a in A:
    if a > m:
        m = a
    elif a > s:
        s = a

for a in A:
    if a == m:
        print(s)
    else:
        print(m)

