k = int(input())
ans = -1
ai = 0
for i in range(1, k + 1):
    ai = (ai * 10 + 7) % k
    if ai == 0:
        ans = i
        break
print(ans)
