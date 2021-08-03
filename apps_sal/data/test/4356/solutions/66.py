n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(m):
    b.append(input())
flag = 0
judge = []
for i in range(n - m + 1):
    judge = []
    for j in range(n - m + 1):
        judge = []
        for k in range(m):
            judge.append(a[i + k][j:j + m])
        if judge == b:
            flag += 1
if flag == 0:
    print("No")
else:
    print("Yes")
