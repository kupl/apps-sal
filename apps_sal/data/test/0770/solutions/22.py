n = int(input())
mailbox = list(map(int, input().split())) + [0]
ans = 0
for i in range(n):
    if mailbox[i] == 1:
        ans += 1
        if mailbox[i + 1] == 0:
            ans += 1
print(max(0, ans - 1))
