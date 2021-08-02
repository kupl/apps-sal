line = input().split(" ")
a = int(line[0])
b = int(line[1])
c = int(line[2])
k = int(line[3])
ans = 0


if a >= k:
    ans = k
else:
    ans += a
    k -= a
    if b < k:
        k -= b
        ans -= k


print(ans)
