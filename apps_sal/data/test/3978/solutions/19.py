ans = 0
n = int(input())
new = [True] * 101
for a in sorted(map(int, input().split())):
    if new[a]:
        ans += 1
        for b in range(a, 101, a):
            new[b] = False
print(ans)
