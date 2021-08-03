n = int(input())
l = [n] * (n + 1)
for c in [int(x) for x in input().split()]:
    l[c] = l[c - 1] - 1
print(min(l))
