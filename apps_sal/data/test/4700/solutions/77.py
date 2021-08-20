(n, m) = list(map(int, input().split()))
h = list(map(int, input().split()))
hoge = [[] for _ in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    hoge[a - 1].append(b - 1)
    hoge[b - 1].append(a - 1)
cnt = 0
for i in range(n):
    if hoge[i]:
        flag = True
        for j in hoge[i]:
            if h[i] <= h[j]:
                flag = False
        if flag:
            cnt += 1
    else:
        cnt += 1
print(cnt)
