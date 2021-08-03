N = int(input())
a = list(map(int, input().split()))

b = [0] * N

if N % 2 == 0:
    even = N // 2
    odd = even - 1
    for i in range(N):
        if i % 2 == 0:
            b[even] = str(a[i])
            even += 1
        else:
            b[odd] = str(a[i])
            odd -= 1
else:
    even = N // 2
    odd = even + 1
    for i in range(N):
        if i % 2 == 0:
            b[even] = str(a[i])
            even -= 1
        else:
            b[odd] = str(a[i])
            odd += 1

print((' '.join(b)))
