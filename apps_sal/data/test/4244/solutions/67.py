N = int(input())
X = list(map(int, input().split()))

ave = 0

for i in X:
    ave += i
if ((ave / N) // 0.5) % 2 == 1:
    ave = (ave // N) + 1
else:
    ave = ave // N

ans = 0
for i in X:
    ans += (ave - i)**2
print(ans)
