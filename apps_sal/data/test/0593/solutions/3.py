n, m = [int(i) for i  in input().split()]
h = [0 for i in range(n)]
for i in range(m):
    s = [int(i) for i  in input().split()]
    h[s.index(max(s))]+=1
print(h.index(max(h))+1)

