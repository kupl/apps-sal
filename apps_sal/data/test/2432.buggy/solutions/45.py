x = int(input())
r = [4, 1, 3, 2, 0, 5]
ans = 0
for i in range(6):
    if x & 1 << i:
        ans |= 1 << r[i]
print(ans)
