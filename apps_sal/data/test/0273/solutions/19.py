(name, surname) = input().split()
ans = name[0]
for i in name[1:]:
    if i < surname[0]:
        ans += i
    else:
        break
ans += surname[0]
print(ans)
