n, m = map(int, input().split())
s = []
N = [0 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    s.append([a,b])
    N[a-1] += 1
    N[b-1] += 1
for j in range(n):
    print(N[j])
