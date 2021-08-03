def inp(): return map(int, input().split())


n, k = inp()
n2 = n

a = [0] * 100
i = 0

while(n2 > 0):
    a[i] = n2 % 2
    n2 //= 2
    i += 1

cnt = i - 1
cnt2 = cnt
sum = 0
arr = [0] * (10**7 + 1)
q = [0] * (10**7 + 1)


for i in range(cnt, -1, -1):
    sum += a[i]
    q[i] = a[cnt - i]

if sum > k:
    print("No")
    quit()

k2 = k - sum

beg = 0
while k2 > 0:
    if(q[beg] <= k2):
        k2 -= q[beg]
        q[beg + 1] += 2 * q[beg]
        q[beg] = 0
        beg += 1
    else:
        break

cnt += 1000

while(q[cnt] == 0):
    cnt -= 1


while k2 > 0:
    q[cnt] -= 1
    q[cnt + 1] += 2
    cnt += 1
    k2 -= 1


print("Yes")

for i in range(beg, cnt + 1):
    for j in range(1, q[i] + 1):
        print(cnt2 - i, '', end='')
