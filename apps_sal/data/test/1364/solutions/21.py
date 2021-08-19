n = int(input())
t = list(map(int, input().split()))
t2 = []
result = 0
cur = 1
for i in range(n - 1):
    if t[i] == t[i + 1]:
        cur += 1
    else:
        t2.append((t[i], cur))
        cur = 1
t2.append((t[-1], cur))
for i in range(len(t2) - 1):
    result = max(result, min(t2[i][1], t2[i + 1][1]))
print(result * 2)
