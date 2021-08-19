n = int(input())

ans = 0
for i in range(100):
    if n - 4 * i >= 0 and (n - 4 * i) % 7 == 0:
        ans += 1

# print(ans)

if ans >= 1:
    print('Yes')
else:
    print('No')
