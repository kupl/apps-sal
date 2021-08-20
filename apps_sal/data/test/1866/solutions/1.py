n = int(input())
for i in range(20):
    if 2 ** i > n:
        pointer = i
        break
a = 2 ** (pointer - 1)
ans = []
for i in range(pointer - 1):
    pointer2 = 0
    k = 2 ** i
    for j in range(a):
        if j % (2 * k) < k:
            ans.append([str(j + 1), str(j + 1 + k)])
for i in range(pointer - 1):
    pointer2 = 0
    k = 2 ** i
    for j in range(a):
        if j % (2 * k) < k:
            ans.append([str(n - j), str(n - j - k)])
print(len(ans))
for i in ans:
    print(' '.join(i))
