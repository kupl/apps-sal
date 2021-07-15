
N = int(input())
D = list(map(int, input().split()))
ans = 0

for i in range(len(D)-1):
    for j in range(i+1, len(D)):
        ans += D[i]*D[j]
print(ans)

