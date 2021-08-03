N, K = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * (N + 1)
r = [0] * (N + 1)
#l[0] = a[1]
#r[-2] = a[-1]
for i in range(N):
    l[i + 1] = l[i] + a[i]
    r[-i - 2] = r[-i - 1] + a[-i - 1]
s = l[-1]

ans = 0

for i in range(N):
    if K > s - r[-i - 1]:
        break
    else:
        c = s - K - r[-i - 1]
        min1 = 0
        max1 = N - i
        while max1 - min1 > 1:
            t = (max1 + min1) // 2
            if l[t] > c:
                max1 = t
            else:
                min1 = t
        ans += min1 + 1
        #print(i, min1)

print(ans)
