N = int(input())
a = list(map(int, input().split()))

avg = round((sum(a) / N))
ans = 0
for i in a:
    ans = ans + (i - avg) * (i - avg)

print(ans)
