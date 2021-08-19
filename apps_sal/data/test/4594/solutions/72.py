N = int(input())
d = [int(input()) for i in range(N)]
l = []
for i in range(N):
    if d[i] not in l:
        l.append(d[i])
print(len(l))
