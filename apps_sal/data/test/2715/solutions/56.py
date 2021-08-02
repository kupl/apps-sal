k = int(input())
max_a = pow(10, 16) + 1000
for i in range(2, 51):
    a = [j + k // i for j in range(i)]
    for j in range(k % i):
        a[-1 - j] += 1
    if max(a) <= max_a:
        print(i)
        print(' '.join(list(map(str, a))))
        return
