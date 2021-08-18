n = int(input())
A = [int(i) for i in input().split()]

A1 = A[0]
A2 = A[1]

c = 0
for ele in A[2:]:
    c ^= ele

d = A1 + A2 - c
if d % 2 == 1:
    print((-1))
else:
    d = d // 2
    flgs = []

    for i in range(41):
        fand = d & (1 << i)
        fxor = c & (1 << i)

        if fand & fxor:
            print((-1))
            break
        elif fand:
            flgs.append(1)
        elif fxor:
            flgs.append(2)
        else:
            flgs.append(0)
    else:
        flgs = flgs[::-1]
        ans = 0
        for i in range(len(flgs)):
            if flgs[i] == 1:
                ans += 2**(41 - i - 1)

        if ans > A1:
            print((-1))
        else:

            for i in range(len(flgs)):
                if flgs[i] == 2:
                    if ans + 2**(41 - i - 1) <= A1:
                        ans += 2**(41 - i - 1)

            if ans == 0:
                print((-1))
            else:
                print((A1 - ans))
