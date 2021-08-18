n, k = map(int, input().split())
sushi = [[int(i) for i in input().split()] for _ in range(n)]
sushi.sort(key=lambda x: x[1], reverse=True)
eaten = [False] * n
d1 = [0]
d2 = [0]
for i in range(n):
    t, d = sushi[i]
    t -= 1
    if eaten[t]:
        d1.append(d1[-1] + d)
    else:
        eaten[t] = True
        d2.append(d2[-1] + d)
ans = 0
for i in range(1, k + 1):
    if k - i >= len(d1):
        continue
    if i >= len(d2):
        continue
    ans = max(ans, d1[k - i] + d2[i] + i * i)
print(ans)
