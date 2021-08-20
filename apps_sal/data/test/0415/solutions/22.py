n = int(input())
r = list(map(int, input().split()))
s = [0] * n
s[0] = r[0]
for i in range(1, n):
    s[i] = s[i - 1] + r[i]
ans = 0
for i in range(n):
    for j in range(i, n):
        num = s[j] - s[i] + r[i]
        time = j + 1 - i
        if num / time > 100 and time > ans:
            ans = time
print(ans)
