n = int(input())
b = list(map(int, input().split()))
b.sort()
ans = float("inf")
j = 1
while (j ** (n - 1) <= 10 ** 10):
    s = 0
    for p in range(n):
        s += abs(j ** p - b[p])
    ans = min(ans, s)
    j += 1
print(ans)











































