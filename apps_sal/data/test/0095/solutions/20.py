n = int(input())
s = [int(i) for i in input().split()]
a = 0
for i in range(1, n):
    if a ==0:
        if s[i] <= s[i-1]:
            a =1
    if a == 1:
        if s[i] < s[i-1]:
            a =2
        if s[i] > s[i - 1]:
            a = 3
            break
    if a == 2:
        if s[i] < s[i-1]:
            a =2
        else:
            a = 3
            break
if a != 3:
    print("YES")
else:
    print("NO")
