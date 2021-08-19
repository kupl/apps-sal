(n, a, b) = list(map(int, input().split()))
ss = list(map(int, input().split()))
s = sum(ss)
s1 = ss[0]
ss = list(reversed(sorted(ss[1:])))
ans = n - 1
for i in range(n):
    if b * s <= a * s1:
        ans = i
        break
    s -= ss[i]
print(ans)
