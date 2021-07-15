n = int(input())
s = input()

cur = 0
ans = 0

for x in s:
    if x == 'x':
        cur += 1
        if cur == 3:
            ans += 1
            cur -= 1
    else:
        cur = 0

print(ans)

