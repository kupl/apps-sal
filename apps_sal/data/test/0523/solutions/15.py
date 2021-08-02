n, m = map(int, input().split())
data = [input() for _ in range(n)]
data_rev = [x[::-1] for x in data]

now = ""
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if data[i] == data_rev[j]:
            now = data[i] + now + data[j]

ans = len(now)
for i in range(n):
    if data[i] == data_rev[i]:
        now2 = data[i]
        for j in range(n):
            if j == i: continue
            for k in range(j + 1, n):
                if k == i: continue
                if data[j] == data_rev[k]:
                    now2 = data[j] + now2 + data[k]
        if ans < len(now2):
            now = now2
            ans = len(now2)

print(ans)
print(now)
