n = int(input())
siv = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    if siv[i] == 0:
        for j in range(i + i, n + 1, i):
            siv[j] = i
    siv[i] = i - siv[i] + 1
result = n
for i in range(siv[n], n + 1):
    result = min(result, siv[i])
print(result)
