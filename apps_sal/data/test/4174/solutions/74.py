(N, X) = map(int, input().split())
L = list(map(int, input().split()))
l = [0]
s = 0
for i in range(N):
    s += L[i]
    if s > X:
        break
    l.append(s)
print(len(l))
