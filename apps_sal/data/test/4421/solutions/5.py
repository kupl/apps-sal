n, k = list(map(int, input().split()))
di = list(map(int, input().split()))
ai = [0] * k
for i in di:
    ai[i % k] += 1
ans = ai[0] // 2
ai[0] = 0
for i in range(1, k):
    num = i
    num2 = k - i
    if num != num2:
        ans += min(ai[num], ai[num2])
    else:
        ans += ai[num] // 2
    ai[num] = 0
    ai[num2] = 0
print(ans * 2)
