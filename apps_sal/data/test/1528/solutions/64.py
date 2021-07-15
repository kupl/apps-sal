N, X = list(map(int, input().split()))
a, p = [1], [1]
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)

# print(a, p)

def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= a[N-1]+1:
        #端のバンズを消すのでXから1引く
        return f(N-1, X-1)
    else:
        #N-1層のパティ数＋真ん中のパティ＋... X-2-a[i]は追加したBPと下側のN-1層の分を引く
        return p[N-1]+1+f(N-1, X-2-a[N-1])
print((f(N, X)))

