N = int(input())
L = list(map(int,input().split()))
ans = 0
lines = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                lines = []
                lines.append(L[i])
                lines.append(L[j])
                lines.append(L[k])
                lines.sort()
                if lines[0]+lines[1] > lines[2]:
                    ans += 1
print(ans)
