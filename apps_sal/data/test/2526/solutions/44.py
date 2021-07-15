#ABC160
x, y, a, b, c = list(map(int, input().split()))
p = list(map(int, input().split())) # list()でリスト化、それを変数に代入。
q = list(map(int, input().split())) # list()でリスト化、それを変数に代入。
r = list(map(int, input().split())) # list()でリスト化、それを変数に代入。

p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)
#print(p)
#print(q)
#print(r)
p = p[:x]
q = q[:y]

eat = p + q + r

eat.sort(reverse = True)
eat = eat[:(x+y)]

print((sum(eat)))
#print(eat)

