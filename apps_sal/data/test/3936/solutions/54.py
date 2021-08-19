

n = int(input())
s = input()
t = input()
u = []

now = 0
while(now < n):
    if(s[now] == t[now]):
        u.append(0)
        now += 1
    else:
        u.append(1)
        now += 2

# print(u)

ans = 1

if(u[0] == 1):
    ans = 6
else:
    ans = 3

for i in range(1, len(u)):
    if(u[i - 1] == 1 and u[i] == 1):
        ans *= 3
    elif(u[i - 1] == 1 and u[i] == 0):
        ans *= 1
    elif(u[i - 1] == 0 and u[i] == 1):
        ans *= 2
    else:
        ans *= 2
    ans %= 10**9 + 7

print(ans)
