def nod(a, b):
    if a > b:
        return nod(b, a)
    elif a == 0:
        return b
    else:
        return nod(b % a, a)


n = int(input())
s = list(map(int, input().split()))
m = max(s)
c = list(filter(lambda x: x>0,map(lambda x: m - x, s)))
d = 0
for j in c:
    d = nod(d,j)
ans = 0
for j in c:
    ans+=j//d
print(ans,d)
