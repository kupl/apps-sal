n = int(input())
aaa = list(map(int, input().split(' ')))
# 1,1,1,2,2, -> 3c2 + 2c2 = 4 + 1 = 4
# 1つ抜くときの数は一発で求まるので。。。
# 1c2=0
# 2c2=1
# 3c2=3
# 4c2=6
# 5c2=10
# 6c2=15
# 7c2=21
# hoge[i] = hoge[i-1] + (i-1)
hoge = [0, 0]
for i in range(2, int(1e6) + 1):
    hoge.append(hoge[i - 1] + (i - 1))


# 1,1,1,2,2, -> 3c2 + 2c2 = 4 + 1 = 4
d = {}
for a in aaa:
    d[a] = d.get(a, 0) + 1
total = sum([hoge[v] for v in list(d.values())])

# 1つ抜く
for i in range(1, n + 1):
    ct = d[aaa[i - 1]]
    print((total - (hoge[ct] - hoge[ct - 1])))
