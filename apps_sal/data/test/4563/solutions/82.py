N = int(input())
A, B = 1, 1
for i in range(N):
    tmpl = list(map(int, input().split()))
    tmp = max(-1 * (-1 * A // tmpl[0]), -1 * (-1 * B // tmpl[1]))
    A, B = tmpl[0] * tmp, tmpl[1] * tmp
print(A + B)
