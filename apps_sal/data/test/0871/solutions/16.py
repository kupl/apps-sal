n, s = map(int, input().split())
chegadas = []
for _ in range(n):
    h, m = map(int, input().split())
    chegadas.append(h * 60 + m)
pos = -1

if chegadas[0] > s:
    print(0, 0)
else:
    for i in range(n - 1):
        if chegadas[i + 1] - chegadas[i] > ((s * 2) + 1):
            pos = i
            break

    t = chegadas[pos] + s + 1
    h, m = int(t / 60), t % 60
    print(h, m)
