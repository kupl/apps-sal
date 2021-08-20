a = int(input())
b = [int(i) for i in input().split()]
c = b.copy()
ans = 0
for i in range(a):
    if b[i] == 1:
        ans += b[i:].count(1)
        break
    ans += 1
ans1 = 0
for i in range(a):
    if b[i] == 1:
        ans1 = max(ans1, b[:i].count(0) + b[i:a].count(1))
print(max(ans, ans1, b.count(0), b.count(1)))
