C = []
for _ in range(3):
    c = list(map(int, input().split()))
    C.append(c)

a = [0, C[1][1] - C[0][1], C[2][1] - C[0][1]]
b = [C[0][0], C[0][1], C[0][2]]

ans = [[a[0] + b[0], a[0] + b[1], a[0] + b[2]], [a[1] + b[0], a[1] + b[1], a[1] + b[2]], [a[2] + b[0], a[2] + b[1], a[2] + b[2]]]

if ans == C:
    print("Yes")
else:
    print("No")
