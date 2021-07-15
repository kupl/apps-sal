n = int(input())
a = [int(i) for i in input().split()]
max_frq = 1
for i in range(n):
    frq = 1
    frq = a.count(a[i])
    if frq >= max_frq:
        max_frq = frq
print(max_frq)
