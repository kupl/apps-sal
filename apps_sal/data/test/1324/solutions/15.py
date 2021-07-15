a = input().split()

ans = 0
s = input()

for i in s:
    if (i == '1'): ans += int(a[0])
    if (i == '2'): ans += int(a[1])
    if (i == '3'): ans += int(a[2])
    if (i == '4'): ans += int(a[3])
    
print(ans)
