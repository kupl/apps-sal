n = int(input())
ans = 0
for i in range(n):
    s = input()
    if s == '++X' or s == 'X++':
        ans += 1
    else:
        ans -= 1
print(ans)
