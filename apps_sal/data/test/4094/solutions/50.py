k = int(input())
ans = -1
s = 7
for i in range(k + 1):
    if s % k == 0:
        ans = i + 1
        break
    s = (s * 10 + 7) % k
print(ans)
