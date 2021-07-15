c1,c2,c3,c4 = list(map(int, input().split()))
n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
suma = sum(min(c1*x, c2) for x in a)
sumb = sum(min(c1*x, c2) for x in b)
print(min(min(suma,c3) + min(sumb, c3), c4))

