(n, m) = list(map(int, input().split()))
dic = {i: 0 for i in range(1, n + 1)}
for i in range(m):
    (a, b) = list(map(int, input().split()))
    dic[a] = dic[a] + 1
    dic[b] = dic[b] + 1
for i in range(1, n + 1):
    print(dic[i])
