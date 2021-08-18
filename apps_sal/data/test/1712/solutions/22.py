n, x, y = list(map(int, input().split()))
cx, cy, A = 0, 0, []
while cx < x or cy < y:
    if (cx + 1) * y > (cy + 1) * x:
        cy += 1
        A.append('Vova')
    elif (cx + 1) * y < (cy + 1) * x:
        cx += 1
        A.append('Vanya')
    else:
        A.append('Both')
        A.append('Both')
        cx += 1
        cy += 1


for _ in range(n):
    a = int(input())
    a -= 1
    a1 = a % (x + y)
    print(A[a1])
