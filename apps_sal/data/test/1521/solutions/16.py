h = []
a = -1
P, N = list(map(int, input().split()))
for i in range(N):
    v = int(input()) % P
    if (v in h) and a == -1:
        a = i + 1
    h.append(v)
print(a)
