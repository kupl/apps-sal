n = int(input())
s=input()
ans = 0
for i in range(n):
    if s[i] in '02468':
        ans += i+1
print(ans)
