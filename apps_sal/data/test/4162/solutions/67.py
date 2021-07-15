n = int(input())
al = list(map(int, input().split()))
ans = 0
for a in al:
    ans += a-1

print(ans)
