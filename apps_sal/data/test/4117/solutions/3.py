n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a = l[i]
            b = l[j]
            c = l[k]
            if a != b and b != c and c < a + b:
                ans += 1
print(ans)
