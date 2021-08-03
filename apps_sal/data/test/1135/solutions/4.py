n = int(input())
a = input()
A = [0] * len(a)
for j in range(len(a)):
    if j % 2 == 0:
        A[-(j // 2 + 1)] = a[len(a) - 1 - j]
    else:
        A[j // 2] = a[len(a) - 1 - j]
print(''.join(map(str, A)))
