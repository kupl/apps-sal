n = int(input())
l = list(map(int, input().split()))
l.sort(key=lambda x: -x)
i = 0
cur = 0
ans = 0
while i < len(l)-1:
    if l[i] == l[i+1] or l[i]-1 == l[i+1]:
        if cur == 0:
            cur = l[i+1]
        else:
            ans += cur*l[i+1]
            cur = 0
        i += 2
    else:
        i += 1
print(ans)

