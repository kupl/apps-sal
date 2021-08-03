n = int(input())
s = input().split()
for i in range(n):
    s[i] = int(s[i])
ans = 0
done = False
for i in range(n):
    if(s[i] == 0):
        continue
    n = s[i + 1:].count(s[i])
    if(n == 1):
        ans += 1
    elif(n > 1):
        print(-1)
        done = True
        break

if(not done):
    print(ans)
