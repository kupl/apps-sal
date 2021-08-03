times = [input() for _ in range(5)]

res = 0
for i in times:
    res += (int(i) // 10) * 10 + (10 if i[-1] != "0" else 0)

time = []
for j in times:
    time.append((int(j[-1]) if j[-1] != "0" else 10))

print(res - 10 + min(time))
