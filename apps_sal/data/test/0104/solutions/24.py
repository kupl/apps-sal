n = int(input())
ai = list(map(int, input().split()))
summ = sum(ai)
summ = summ % 2 + summ // 2
summ2 = 0
ans = 0
for i in range(n):
    summ2 += ai[i]
    if summ2 >= summ:
        ans = i + 1
        break
print(ans)
