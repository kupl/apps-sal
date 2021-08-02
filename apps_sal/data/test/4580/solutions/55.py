N = int(input())
rate = [1, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
p = [0] * 9

A = [int(a) for a in input().split(" ")]
A.sort()

j = 0
for i in range(len(A)):
    while j < 8:
        if rate[j] <= A[i] < rate[j + 1]:
            p[j] = 1
            break
        else:
            j += 1
    else:
        p[8] = len(A[i:])
        break

print((str(max([sum(p[:8]), 1])) + " " + str(sum(p))))
