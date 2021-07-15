m = int(input())

zeros = {}
z = 0
i = 5
while z <= m:
    i_temp = i
    while i_temp % 5 == 0:
        i_temp //= 5
        z += 1

    zeros[z] = i
    i += 5

z = zeros.get(m, None)
if z is None:
    print(0)
else:
    x = m + 1
    while zeros.get(x, None) is None:
        x += 1
    print(5)
    for i in range(zeros[m], zeros[x]):
        print(i, end=" ")
    print()
