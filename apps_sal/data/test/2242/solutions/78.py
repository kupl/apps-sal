S = str(input())
N = len(S)
b = [0] * 2019
count = 0
b[0] = 1
t = 0
k = 1
if len(S) < 4:
    print(0)
else:
    t = int(S[-1])
    b[t] += 1
    for i in range(1, N):
        k = k * 10 % 2019
        t = (k * int(S[-i - 1]) + t) % 2019
        b[t] += 1
    for i in b:
        count += i * (i - 1) // 2
    print(count)
