n, h = list(map(int, input().split()))

atk = []
ans = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    atk.append((a, 0))
    atk.append((b, 1))

atk.sort(key=lambda x: x[0], reverse=True)

for blade in atk:
    if blade[1] == 0:
        break
    else:
        h = max(0, h - blade[0])
        ans += 1
        if h <= 0:
            break

print((ans - (-h // blade[0])))
