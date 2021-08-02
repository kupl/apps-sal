
N = int(input())
AU = list(map(int, input().split()))
AD = list(map(int, input().split()))

AUS = [AU[0]]
ADS = [AD[-1]]

for i in range(1, N):
    AUS.append(AUS[-1] + AU[i])
    ADS.append(ADS[-1] + AD[-1 - i])

ADS.reverse()

ans = 0
for i in range(N):
    temp = AUS[i] + ADS[i]
    ans = max(ans, temp)

print(ans)
