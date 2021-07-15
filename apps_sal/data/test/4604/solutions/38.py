N = int(input())
a = list(map(int, input().split()))
Sum = 1
mod = 1000000007

a.sort()
data = []
if N % 2 == 0:
    for i in range(int(N / 2)):
        data.append(1 + i * 2)
        data.append(1 + i * 2)
else:
    data.append(0)
    for i in range(1, N // 2 + 1):
        data.append(i * 2)
        data.append(i * 2)

if a == data:
    for i in range(N // 2):
        Sum *= 2
        Sum %= mod
    print(Sum)
else:
    print((0))

