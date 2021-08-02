K = int(input())
summ = 49 * 50 + K
a, b = summ // 50, summ % 50
low = (summ - b * 51) // 50
high = low + 51
ans = [low] * 50
for i in range(b):
    ans[i] += 51
print(50)
print(*ans)
