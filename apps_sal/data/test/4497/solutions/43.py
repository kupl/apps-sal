
N = int(input())
N2 = N
a = []

for i in range(N):
    count = 0
    if i != 0:
        tmp = N
        while tmp % 2 == 0:
            tmp = tmp / 2
            count += 1

        N = N - 1
    a.append(count)

max_value = max(a)

ind = a.index(max_value)

if N2 == 1:
    print((1))
else:
    print((N2-ind+1))

