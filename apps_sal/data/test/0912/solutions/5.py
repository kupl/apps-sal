t = int(input())
for _ in range(t):
    n, s, k = list(map(int, input().split()))
    c = set(map(int, input().split()))
    l, u = s, s
    for i in range(10000):
        if (l not in c) or (u not in c):
            print(i)
            break
        if l > 1:
            l -= 1
        if u < n:
            u += 1

