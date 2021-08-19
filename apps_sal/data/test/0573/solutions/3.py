n = int(input())
a1 = 0
a2 = 0
ans = 0
s = input().split()
for i in range(n):
    if s[i] == '1':
        a1 += 1
    else:
        a2 += 1
while a1 >= 1 and a2 >= 1:
    ans += 1
    a1 -= 1
    a2 -= 1
while a1 >= 3:
    ans += 1
    a1 -= 3
print(ans)
