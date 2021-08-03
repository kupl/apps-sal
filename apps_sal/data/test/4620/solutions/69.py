n = int(input())
l = [0] * n
for i in range(1, n):
    c, s, f = map(int, input().split())
    for j in range(i):
        l[j] = max(-l[j] // f * -f, s) + c
for i in l:
    print(i)
