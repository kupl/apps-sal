n, m = list(map(int, input().split()))
s = list(input())
s.reverse()
for i in range(m):
    s.append("1")
p = 0
ans = []
while p < n:
    p += m
    cnt = m
    while s[p] == "1":
        p -= 1
        cnt -= 1
        if cnt == 0:
            print((-1))
            return
    ans.append(cnt)
ans.reverse()
print((*ans))
