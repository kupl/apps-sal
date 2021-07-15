ans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    if sum(u) == 0:
        ans.append("NO")
        continue
    u.sort()
    if sum(u) > 0:
        u.reverse()
    ans.append("YES")
    ans.append(' '.join(map(str, u)))
print('\n'.join(ans))

