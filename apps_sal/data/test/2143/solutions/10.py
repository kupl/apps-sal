n = int(input())
cl = list(map(int, input().split()))
dl = [0] * (2 * 10 ** 5 + 1)
for i in range(n):
    for j in range(i + 1, n):
        d = cl[i] + cl[j]
        dl[d] += 1
mx = max(dl)
print(mx)
