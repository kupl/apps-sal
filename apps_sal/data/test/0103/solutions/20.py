n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [1001]

ans = 0
for i in range(len(a)):
    for j in range(i + 3, len(a) + 1):
        if a[i : j] == list(range(a[i], a[i] + j - i)):
            ans = max(ans, j - i - 2)

print(ans)
