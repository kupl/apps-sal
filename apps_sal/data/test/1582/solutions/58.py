N = int(input())

count = [[0] * 10 for _ in range(10)]
for i in range(1, N + 1):
    s = str(i)
    head = int(s[0])
    tail = int(s[-1])
    count[head][tail] += 1

ans = 0
for a in range(1, N + 1):
    s = str(a)
    head = int(s[0])
    tail = int(s[-1])
    ans += count[tail][head]
print(ans)
