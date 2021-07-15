n = int(input())
s = input()
cnt = 0
for i in range(1,n):
    if s[i] == s[i-1]: cnt += 1

print(cnt)


