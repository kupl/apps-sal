#from operator import itemgetter
# int(input())
# map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
n = int(input())
ai = list(map(int, input().split()))
ans = 0
for i in range(2, n):
    if ai[i - 2] == ai[i] and ai[i] == 1 and ai[i - 1] == 0:
        ai[i] = 0
        ans += 1
print(ans)
