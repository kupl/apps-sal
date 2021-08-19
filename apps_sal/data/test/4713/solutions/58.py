n = int(input())
s = input()
c = 0
ans = 0
for i in list(s):
    if i == 'I':
        c += 1
    else:
        c -= 1
    ans = max(ans, c)
print(ans)
