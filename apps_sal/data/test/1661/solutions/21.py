(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in a:
    if b:
        if b[0] >= i:
            c += 1
            b.remove(b[0])
print(c)
