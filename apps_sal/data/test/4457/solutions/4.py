from sys import stdin, stdout  



n = int(input())

D = (list(map(int, input().split())))

for i in range(n):
    D[i] = [D[i], i]
D.sort(reverse=True)
ans = 0

for i, d in enumerate(D):
    ans += d[0]*i + 1
    
print(ans)

for d in D:
    print(d[1] + 1, end= ' ')
