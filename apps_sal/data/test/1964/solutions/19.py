d, n = 30001, int(input())
t = list(map(int, input().split()))
for i in range(n):
    s = sum(map(int, input().split())) + 3 * t[i]
    if s < d: d = s
print(d * 5)
