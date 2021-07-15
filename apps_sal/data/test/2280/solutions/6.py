n = int(input())
for i in range(n):
    p = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    if p == 2:
        print(0)
        continue
    k = a[-2] - 1
    print(min(k, p - 2))
