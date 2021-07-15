n = int(input())
st = list(map(int, input().split()))
x = list(map(int, input().split()))
a = min(x)-1
b = max(x)-1
if a == b:
    print(0)
    return

al = sum(st)

f = sum(st[a:b])
s = al - f

print(min(f, s))

