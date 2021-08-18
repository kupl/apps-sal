N = int(input())

l = []
l = list(map(int, input().split()))

s = sum(l)
n = int((s / N * 2 + 1) // 2)

ans = 0
for e in l:
    ans += (e - n)**2

print(ans)
