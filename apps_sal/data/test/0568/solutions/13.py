n = int(input())
M = 10 ** 9 + 7
t1 = 0
t2 = 0
for i in range(1,4):
        for j in range(1,4):
                for k in range(1,4):
                        if i + j + k == 6:
                                t1 += 1
                        t2 += 1
a1 = 1
a2 = 1
for i in range(n):
        a1 = (a1 * t1) % M
        a2 = (a2 * t2) % M
ans = ((a2 - a1) % M + M) % M
print(ans)

