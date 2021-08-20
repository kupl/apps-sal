n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))
a.sort()
ans = 0
ind = 0
while ind < n and a[ind][0] < 0:
    ind += 1
k = 1
sign = -1
while 0 <= ind < n:
    ans += a[ind][1]
    ind += sign * k
    k += 1
    sign = -sign
second_ans = 0
ind = n - 1
while ind >= 0 and a[ind][0] > 0:
    ind -= 1
k = 1
sign = 1
while 0 <= ind < n:
    second_ans += a[ind][1]
    ind += sign * k
    k += 1
    sign = -sign
print(max(ans, second_ans))
