(n, k) = map(int, input().split())
s = 0
o = 1
b = ''
for i in range(k + 1):
    b += str(i)
for i in range(n):
    o = 1
    a = input()
    for j in b:
        if not j in a:
            o = 0
    if o == 1:
        s += 1
print(s)
