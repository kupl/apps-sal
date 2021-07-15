n,c = map(int,input().split())
p = list(map(int,input().split()))
t = list(map(int,input().split()))
x = 0
y = 0
res = 0
for i,j in enumerate(p):
    res += c*t[i]
    x += max(0,j - res)
p = p[::-1]
t = t[::-1]
res = 0
for i,j in enumerate(p):
    res += c*t[i]
    y += max(0,j - res)

if x > y:
    print("Limak")
elif x == y:
    print("Tie")
else:
    print("Radewoosh")
