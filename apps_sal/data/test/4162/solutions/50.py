N = int(input())
a = list(map(int, input().split()))

ans = 0
for x in a:
    ans += x - 1
print(ans)
