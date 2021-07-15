n = int(input())
a = [int(i) for i in input().split()]
p = [0] * 3
for i in range(n):
    p[a[i]] += 1
ans = min(p[1], p[2])
p[1] -= ans
p[2] -= ans
ans += p[1] // 3
print(ans)
