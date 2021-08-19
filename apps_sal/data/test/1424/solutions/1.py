(n, m, k) = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
fedya = int(input())
fedya = str(bin(fedya)[2:])
fedya = '0' * (n - len(fedya)) + fedya
ans = 0
for bb in a:
    bbb = str(bin(bb)[2:])
    bbb = '0' * (n - len(bbb)) + bbb
    delta = 0
    for i in range(n):
        if bbb[i] != fedya[i]:
            delta += 1
    if delta <= k:
        ans += 1
print(ans)
