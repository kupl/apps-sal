N = int(input())
A = [list(map(int, (input().split(' ')))) for i in range(N)]

hoge = [sum(a) for a in A]
fuga = [a[0] - a[1] for a in A]
print((max(max(hoge) - min(hoge), max(fuga) - min(fuga))))
