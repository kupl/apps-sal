N = int(input())
p = list(map(int, input().split()))
n = [i+1 for i in range(N)]
for i in range(N):
    if n[i] != p[i]:
        for j in range(N -i -1):
            if n[i+j+1] != p[i+j+1]:
                p[i], p[i+j+1] = p[i+j+1], p[i]
                break
if n == p:
    print("YES")
else:
    print("NO")
