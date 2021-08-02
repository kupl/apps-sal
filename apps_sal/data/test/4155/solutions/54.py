N = int(input())
h = list(map(int, input().split()))
s = 0
while h != [0] * N:
    c = 0
    for i in range(N - 1):
        if h[i] != 0 and h[i + 1] == 0:
            c += 1
    if h[N - 1] != 0:
        c += 1
    for i in range(N):
        if h[i] != 0:
            h[i] -= 1
    s += c
print(s)
