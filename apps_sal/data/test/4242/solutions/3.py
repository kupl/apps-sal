(a, b, k) = list(map(int, input().split()))
cnt = 0
ans = 0
l = []
for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        l.append(i)
ans = l[-1 * k]
print(ans)
