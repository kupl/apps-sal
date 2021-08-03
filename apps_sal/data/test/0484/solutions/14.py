n, a, b = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def sqr(f, s):

    for i in range(3):
        if (a >= f[0] + s[0] and b >= max(f[1], s[1])) or (b >= f[0] + s[0] and a >= max(f[1], s[1])):
            return f[0] * f[1] + s[0] * s[1]
        elif (a >= max(f[0], s[0]) and b >= f[1] + s[1]) or (b >= max(f[0], s[0]) and a >= f[1] + s[1]):
            return f[0] * f[1] + s[0] * s[1]

        elif(i == 0):
            f[0], f[1] = f[1], f[0]
        elif (i == 1):
            f[0], f[1] = f[1], f[0]
            s[0], s[1] = s[1], s[0]

    return 0


maxi = 0
for i in range(n):
    for j in range(n):
        if i != j:
            maxi = max(maxi, sqr(A[i], A[j]))
print(maxi)
