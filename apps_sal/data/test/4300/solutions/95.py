n = int(input())
oisi = list(map(int, input().split()))
total = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        total += oisi[i] * oisi[j]
print(total)
