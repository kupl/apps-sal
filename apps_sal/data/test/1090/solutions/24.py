n, k = list(map(int, input().split()))
s = input()

x = 0
y = 0
ans = n

# if s[0]=="L":
#     y+=1
# if s[-1]=="R":
#     y+=1
# ans+=y
# s="R"+s+"L"
for i in range(n - 1):
    if s[i:i + 2] == "RL":
        x += 1
        # x+=1
        # ans-=2
    if s[i:i + 2] == "LR":
        y += 1

x = max(x - k, 0)
y = max(y - k, 0)
ans = ans - x - y - 1
# ans+=min(k,x-1)*2
#
# if (k-x+1>0)&(y==0):
#     ans+=1

print(ans)
