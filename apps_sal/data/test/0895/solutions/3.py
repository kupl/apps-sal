n = int(input())
p = list(map(int, input().split()))
T = int(input())
p.sort()
fs = 0
maxx = 0
for i in range(n):
    while fs < n and p[fs] - p[i] <= T:
        fs += 1
    maxx = max(maxx, fs - i)
print(maxx)
