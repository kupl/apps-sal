n, k = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * 40
for i in A:
    s = format(i, "40b")
    for j in range(40):
        if s[-1 - j] == "1":
            B[j] += 1
C = [0] * 40
for i in range(40):
    if B[-1 - i] < n / 2:
        C[i] = 1
    else:
        C[i] = 0
AA = []
a = 0
for i in range(40):
    if C[i] == 1:
        if a + 2**(39 - i) > k:
            continue
        b = a
        for j in range(i + 1, 40):
            if C[j] == 1:
                b = b + 2**(39 - j)
        AA.append(b)
        a = a + 2**(39 - i)
AA.append(a)
ans = 0
for i in AA:
    a = 0
    for j in A:
        a = a + (i ^ j)
    if a > ans:
        ans = a
print(ans)
