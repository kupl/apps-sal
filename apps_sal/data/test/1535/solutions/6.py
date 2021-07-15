n, x, y = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
S = set()
B = []
for elem in A:
    i = 0
    while i < len(B) and B[i][0] * elem[0] + B[i][1] * elem[1] + B[i][2] != 0:
        i += 1
    if i == len(B):
        a = elem[1] - y
        b = x - elem[0]
        c = -(a * x + b * y)
        B.append((a, b, c))
print(len(B))
