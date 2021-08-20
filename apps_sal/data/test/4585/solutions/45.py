x = int(input())
ans = 0
for t in range(10 ** 9):
    if t * (1 + t) // 2 >= x:
        ans = t
        break
print(ans)
