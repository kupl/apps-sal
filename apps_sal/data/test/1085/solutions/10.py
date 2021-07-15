N = int(input())
ans = 0
wnasi = []
for i in range(1, int(pow(N - 1, 0.5)) + 1):
    if (N - 1) % i == 0:
        wnasi.append(i)
        if i != (N - 1) // i:
            wnasi.append((N - 1) // i)
ans += len(wnasi) - 1
wari = []
for i in range(2, int(pow(N, 0.5)) + 1):
    if N % i == 0:
        wari.append(i)
        if i != N // i:
            wari.append(N // i)

for i in wari:
    if i == 1:
        continue
    tmpN = N
    while True:
        if tmpN % i == 0:
            tmpN //= i
        else:
            if tmpN % i == 1:
                ans += 1
            break

print(ans + 1)
