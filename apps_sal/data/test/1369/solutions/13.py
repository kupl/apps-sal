n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
if n == 2:
    print(((x[0] - x[1])**2 + (y[0] - y[1])**2)**(1 / 2) / 2)
else:
    ans = 10**5
    for i in range(n - 1):
        for j in range(i + 1, n):
            xc = (x[i] + x[j]) / 2
            yc = (y[i] + y[j]) / 2
            r = ((x[i] - xc)**2 + (y[i] - yc)**2)**(1 / 2)
            rr = max(r * 1.000000999, r + 0.000000999)
            aa = 0
            for l in range(n):
                if ((x[l] - xc)**2 + (y[l] - yc)**2)**(1 / 2) > rr:
                    aa = 1
            if aa == 0:
                if r < ans:
                    ans = r
    A = [0] * 3
    B = [0] * 3
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            A[0] = x[j] - x[i]
            A[1] = y[j] - y[i]
            A[2] = A[0] * (x[i] + x[j]) / 2 + A[1] * (y[i] + y[j]) / 2
            for k in range(j + 1, n):
                B[0] = x[k] - x[i]
                B[1] = y[k] - y[i]
                B[2] = B[0] * (x[i] + x[k]) / 2 + B[1] * (y[i] + y[k]) / 2
                if A[0] * B[1] == A[1] * B[0] and A[0] * B[1] != 0:
                    r = ((max(x[i], x[j], x[k]) - min(x[i], x[j], x[k]))**2 + (max(y[i], y[j], y[k]) - min(y[i], y[j], y[k]))**2)**(1 / 2) / 2
                    xc = (max(x[i], x[j], x[k]) + min(x[i], x[j], x[k])) / 2
                    yc = (max(y[i], y[j], y[k]) + min(y[i], y[j], y[k])) / 2
                elif A[0] == B[0] == 0:
                    r = (max(y[i], y[j], y[k]) - min(y[i], y[j], y[k])) / 2
                    xc = x[i]
                    yc = (max(y[i], y[j], y[k]) + min(y[i], y[j], y[k])) / 2
                elif A[1] == B[1] == 0:
                    r = (max(x[i], x[j], x[k]) - min(x[i], x[j], x[k])) / 2
                    yc = y[i]
                    xc = (max(x[i], x[j], x[k]) + min(x[i], x[j], x[k])) / 2
                else:
                    xc = (A[2] * B[1] - A[1] * B[2]) / (A[0] * B[1] - A[1] * B[0])
                    yc = (A[0] * B[2] - A[2] * B[0]) / (A[0] * B[1] - A[1] * B[0])
                    r = ((x[i] - xc)**2 + (y[i] - yc)**2)**(1 / 2)
                aa = 0
                rr = max(r * 1.000000999, r + 0.000000999)
                for l in range(n):
                    if ((x[l] - xc)**2 + (y[l] - yc)**2)**(1 / 2) > rr:
                        aa = 1
                if aa == 0:
                    if r < ans:
                        ans = r
    print(ans)
