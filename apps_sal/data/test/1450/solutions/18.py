s = input()
ans = []
ones = 0
for i in s:
    if i != '1':
        ans += [i]
    else :
        ones += 1
i = 0
n = len(ans)
while i < n and ans[i] != '2':
    print(0,end="")
    i += 1
print("1"*ones,end="")

while i < n:
    print(ans[i],end="")
    i+= 1

