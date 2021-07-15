N = int(input())
Alst = list(map(int, input().split()))
Blst = list(map(int, input().split()))
Clst = list(map(int, input().split()))

ans = sum(Blst)

for i in range(N-1):
    if Alst[i] + 1 == Alst[i+1]:
        ans += Clst[Alst[i]-1]

print(ans)
