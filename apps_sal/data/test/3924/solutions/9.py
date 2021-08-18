n, k = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]
x = 0
s = 0
ans = 0
for i in range(n):
    if x == 0:
        s += lst[i]
        ans += (s // k)
        s = s % k
        if s > 0:
            x = 1
    elif x == 1:
        if (s + lst[i] < k):
            ans += 1
            s = 0
            x = 0
        else:
            s += lst[i]
            ans += s // k
            s = s % k
            if s > 0:
                x = 1
            else:
                x = 0


if(s > 0):
    print(ans + 1)
else:
    print(ans)
