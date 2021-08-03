n, a, b = list(map(int, input().split()))
# Pick any i,j such that i*a + j*b == n
choose = None
for i in range(n + 1):
    if a * i > n:
        continue
    j = (n - a * i) // b
    if i * a + j * b == n:
        choose = (i, j)
if choose:
    i, j = choose
    arr = []
    for t in range(i):
        arr.append(a)
    for t in range(j):
        arr.append(b)
    got = 0
    answer = []
    # print(arr)
    for x in arr:
        cur = []
        for i in range(got + 1, got + x + 1):
            cur.append(i)
        cur = cur[1:] + [cur[0]]
        got += x
        answer += cur
    print(' '.join(map(str, answer)))

else:
    print(-1)
