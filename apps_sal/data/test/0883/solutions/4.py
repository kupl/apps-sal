3

n = int(input())
s = sum(map(int, input().split()))
ans = 0
for i in range(1, 6):
    ans += (s + i) % (n + 1) != 1
print(ans)
