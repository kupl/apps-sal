n, m = list(map(int, input().split()))
s = input()
now = 0
MIN = 0
ans = []
while now < n:
    for i in range(min(n - now, m), 0, -1):
        nex = now + i
        if s[nex] == "0":
            now = nex
            MIN += 1
            break
    else:
        print((-1))
        return
now = 0
while now < n:
    for i in range(min(n - now, m), 0, -1):
        nex = now + i
        if s[n - nex] == "0":
            now = nex
            ans.append(i)
            break
print((*reversed(ans)))
