n = int(input())
d = dict()
l = [int(j) for j in input().split()]
l2 = [int(j) for j in input().split()]
f = 0
c = 0
for i in range(n):
    t = l[i]
    if f == n:
        break
    if not(t in d):
        while l2[c] != t and c < n:
            k = l2[c]

            if not(k in d):
                d[k] = 1
                f += 1
            c += 1
        c += 1
print(f)
