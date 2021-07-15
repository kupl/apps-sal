n = int(input())
s = sum(map(int, input().split()))
ans = 0
for i in range(5):
    ans += 1 if (s + i) % (n + 1) else 0
print(ans)
