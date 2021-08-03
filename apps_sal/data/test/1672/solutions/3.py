
n = int(input())

ans = 0
c = '0'
for i in range(n):
    s = input()
    if(i == 0 or s[0] == c):
        ans += 1
        c = s[1]

print(ans)
