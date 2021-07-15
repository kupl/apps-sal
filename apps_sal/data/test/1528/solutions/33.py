# 解説AC
n,x = map(int,input().split())
b,p = [1],[1]
for i in range(n):
    # レベルNバーガーの層の総数
    b.append(b[i] * 2 + 3)
    # レベルNバーガーのPの総数
    p.append(p[i] * 2 + 1)
# 再帰関数でPの総数を調べる
# レベル0バーガーから1,2...Nまでの下からX層のPの総数を順番に調べる
def pate(n,x):
    if n == 0:
        if x <= 0:
            return 0
        else:
            return 1
    elif x <= 1 + b[n-1]:
        return pate(n-1,x-1)
    else:
        return p[n-1] + 1 + pate(n-1,x-2-b[n-1])
print(pate(n,x))
