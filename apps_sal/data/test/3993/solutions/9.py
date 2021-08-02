n, m, k = map(int, input().split())
p = list(map(int, input().split()))

page = k * ((p[0] - 1) // k + 1)
j = 0
k_op = 0
cfnt = 0

while (j < m):
    if (p[j] - cfnt > page):
        cfnt = j
        page = k * ((p[j] - cfnt - 1) // k + 1)
        k_op += 1
        j -= 1
    j += 1

print(k_op + 1)
