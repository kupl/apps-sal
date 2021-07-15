n = int(input())
c = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1, n+1):
    s = str(i)
    c[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(1, n+1):
    s = str(i)
    ans += c[int(s[-1])][int(s[0])]
print(ans)
