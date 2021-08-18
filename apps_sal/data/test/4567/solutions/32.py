n = int(input())
sl = []
for i in range(n):
    sl.append(int(input()))

total = sum(sl)
sl.sort()

if total % 10 == 0:
    ans = 0
    for i in range(n):
        if sl[i] % 10 != 0:
            ans = total - sl[i]
            break
else:
    ans = total
print(ans)
