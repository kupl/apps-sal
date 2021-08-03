n = int(input())
k = list(map(int, input().split()))
r = 51500
for i in range(n):
    m = list(map(int, input().split()))
    p = len(m) * 15 + 5 * sum(m)
    r = min(r, p)
print(r)
