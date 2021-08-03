n, k = list(map(int, input().split()))
ci = list(map(int, input().split()))
idi = list(map(int, input().split()))
idi += [n + 1]
num3 = sum(ci)
num = 0
num2 = 0
ans = 0
num4 = 0
if idi[num] == 1:
    num += 1
    num2 += ci[0]
    ans += (num3 - num2) * ci[0]
    num4 = 0
else:
    ans += ci[1] * ci[0]
    num4 = 1
for i in range(2, n):
    if idi[num] == i:
        num2 += ci[i - 1]
        ans += (num3 - num2 - ci[i - 2] * num4) * ci[i - 1]
        num += 1
        num4 = 0
    else:
        ans += ci[i] * ci[i - 1]
        num4 = 1
if idi[k - 1] == n:
    num2 += ci[n - 1]
    ans += (num3 - num2 - ci[n - 2] * num4) * ci[n - 1]
    num += 1
if idi[0] != 1 and idi[k - 1] != n:
    ans += ci[n - 1] * ci[0]
print(ans)
