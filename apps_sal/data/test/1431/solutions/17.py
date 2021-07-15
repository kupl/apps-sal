n = int(input())
a = list(map(int, input().split()))
a = [0] + a
l = [0]*(n + 1)

for i in range(n, 0, -1):
    if i > 0 - -n//2:
        l[i] = a[i]
    else:
        if a[i] != sum(l[i::i])%2:
            l[i] = 1

print(l.count(1))

for i in range(1, n + 1):
    if l[i] == 1:
        print(i)
