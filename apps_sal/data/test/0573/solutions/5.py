n = map(int, input().split())
a = list(map(int, input().split()))
c2 = sum([1 for i in a if i == 2])
c1 = sum([1 for i in a if i == 1])
ans = 0
ans = min(c1, c2)
c2 -= ans
c1 -= ans
ans += c1 // 3
print(ans)
