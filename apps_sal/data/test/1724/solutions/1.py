n = int(input())
a = list(map(int, input().split()))
sum = [0] * (n + 1)
sum[1] = a[0]
sum[0] = 0
for i in range(2, n + 1):
    sum[i] = sum[i - 1] + a[i - 1]
s = input()
maxi = 0
cur = n - 1
tmp = 0
while (cur >= 0):
    if s[cur] == '1':
        x = sum[cur] + tmp
        if x > maxi:
            maxi = x
        tmp += a[cur]
    cur -= 1
if tmp > maxi:
    maxi = tmp
print(maxi)
