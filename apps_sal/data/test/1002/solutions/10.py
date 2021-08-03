n, t = list(map(int, input().split()))
s = list(map(int, input().split()))

if sum(s) + (len(s) - 1) * 10 > t:
    print(-1)
else:
    print(((len(s) - 1) * 2) + (t - sum(s) - (len(s) - 1) * 10) // 5)
