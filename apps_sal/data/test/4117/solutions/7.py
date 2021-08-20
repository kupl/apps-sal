n = int(input())
l = list(map(int, input().split()))
ls = sorted(l)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            (a, b, c) = (ls[i], ls[j], ls[k])
            if len(set([a, b, c])) == 3:
                if a + b > c:
                    ans += 1
print(ans)
