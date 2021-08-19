(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = 0
sorted_l = l.sort()
l.reverse()
for i in range(0, k):
    ans += l[i]
print(ans)
