(n, m, k) = map(int, input().split())
A = list(map(int, input().split()))
B = list(enumerate(A))
B.sort(key=lambda x: x[1])
B.reverse()
LIST = [0] * n
ANS = 0
for i in range(m * k):
    LIST[B[i][0]] = 1
    ANS += B[i][1]
ANSLIST = []
count = 0
for i in range(n):
    if LIST[i] == 1:
        count += 1
    if count == m:
        ANSLIST.append(i + 1)
        count = 0
print(ANS)
for a in ANSLIST[:-1]:
    print(a, end=' ')
