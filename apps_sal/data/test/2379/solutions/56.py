n, k, c = list(map(int, input().split()))
s = input()

workL = [0] * (n + 1)
workR = [0] * (n + 1)

cnt = 0
left = 0

while left < n:
    if s[left] == 'o':
        workL[left + 1] += 1
        cnt += 1
        left += c
    left += 1

cnt = 0
right = n - 1
while right >= 0:
    if s[right] == 'o':
        workR[right] += 1
        cnt += 1
        right -= c
    right -= 1

for i in range(n - 1):
    workL[i + 1] += workL[i]
for i in range(n - 1, 0, -1):
    workR[i - 1] += workR[i]


print(("\n".join(
    map(str, [i + 1 for i in range(n) if workL[i] + workR[i + 1] < k]))))

