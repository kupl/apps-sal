n, m = map(int, input().split())
s = input()[::-1]
ans = []
now = 0
while now<n:
    for i in range(min(m, n-now), 0, -1):
        if s[now+i]=='0':
            now += i
            ans.append(i)
            break
    else:
        print(-1)
        return
print(*ans[::-1])
