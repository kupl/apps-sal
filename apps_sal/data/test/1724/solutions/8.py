n = int(input())
a = list(list(map(int, input().split())))
m = input()
s = [int(i) for i in m]
max = 0
sum = 0
for k in range(n):
    sum += a[k] * s[k]
if sum > max:
    max = sum

for i in range(1, n):
    p = s[i]
    q = s[i - 1]
    if p and q == 0:
        sum -= a[i]
        s[i] = 0
        for j in range(i - 1, -1, -1):
            if s[j]:
                break
            sum += a[j]
            s[j] = 1
        if sum > max:
            max = sum


print(max)
