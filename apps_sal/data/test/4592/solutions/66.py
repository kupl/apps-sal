n = int(input())
temp = [1, 1] + [0] * (n - 2)
for i in range(3, n + 1):
    for j in range(2, i):
        while i % j == 0:
            i = i // j
            temp[j - 1] += 1
    if i != 1:
        temp[i - 1] += 1
ans = 1
for i in range(n - 1):
    ans = (ans * (temp[i + 1] + 1)) % (10**9 + 7)
print(ans)
