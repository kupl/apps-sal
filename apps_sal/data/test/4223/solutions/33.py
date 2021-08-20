n = int(input())
s = input()
ans = 0
pc = ''
for c in s:
    if c != pc:
        ans += 1
    pc = c
print(ans)
