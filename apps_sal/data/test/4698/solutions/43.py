n = int(input())
t = tuple(map(int, input().split()))
m = int(input())
x = [list(map(int, input().split())) for _ in range(m)]

i = 0
for x[i] in x:
    l = list(t)
    j = x[i][0] - 1  # インデックス
    k = x[i][1]  # 置換元
    i += i
    l[j] = k
    print(sum(l))
