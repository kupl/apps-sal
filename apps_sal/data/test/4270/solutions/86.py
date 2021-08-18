N = int(input())
V = sorted(list(map(int, input().split())))

ans = (V[0] + V[1]) / 2
for i in range(2, len(V)):
    ans = (ans + V[i]) / 2
print(ans)
