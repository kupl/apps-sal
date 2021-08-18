
S = str(input())[::-1]
N = len(S)
counter = [0] * 2019
counter[0] = 1
ans = 0
num, d = 0, 1
for c in S:
    num += int(c) * d
    num %= 2019
    d *= 10
    d %= 2019
    counter[num] += 1
for i in counter:
    ans += i * (i - 1) // 2
print(ans)
