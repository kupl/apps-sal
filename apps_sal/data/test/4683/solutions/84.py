mod = 10**9 + 7
n = int(input())
a = [int(i) for i in input().split()]
s = sum(a)
out = 0
for i in a:
    s -= i
    out += s * i
    out %= mod
print(out)
