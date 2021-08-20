N = int(input())
l = [0] * N
for i in range(N - 1):
    (c, s, f) = map(int, input().split())
    l[i] = c + s
    for j in range(i):
        l[j] = max(l[j], s, -(-l[j] // f) * f) + c
for i in l:
    print(i)
