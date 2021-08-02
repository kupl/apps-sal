n = int(input())
l = [int(x) for x in input().split(" ")]
s = [1 for i in range(n)]

p = n - 1
q = n - 1

while p > 0:
    while q > p - l[p] and q > 0:
        q -= 1
        s[q] = 0
    p -= 1
    q = min(p, q)

print(sum(s))
