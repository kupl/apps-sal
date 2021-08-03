n, m = map(int, input().split())
if m >= 1:
    gr = list(map(int, input().split()))
    gr.sort()
k = 1
if (m >= 1 and gr[0] == 1) or (m >= 1 and gr[m - 1]) == n:
    print('NO')
else:
    for i in range(m - 2):
        if gr[i] == gr[i + 1] - 1 == gr[i + 2] - 2:
            print('NO')
            k = 0
            break
    if k == 1:
        print('YES')
