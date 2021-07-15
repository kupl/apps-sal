from collections import defaultdict

n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

r = 0
s = ""
for i in x:
    r += i
    s += str(r // m) + " "
    r %= m

print(s)

