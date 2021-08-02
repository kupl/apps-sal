n = int(input())
x = [0] * n
for i in range(n):
    x[i] = input()
x.sort(key=lambda x: len(x))
for i in range(n - 1):
    for j in range(i + 1, n):
        if x[i] not in x[j]:
            print('NO')
            return
print('YES')
for i in x:
    print(i)
