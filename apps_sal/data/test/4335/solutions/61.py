n = int(input())
s = list(input())
a = 1
if len(s)%2==1:
    a = 0
for b in range(int(len(s)/2)):
    if a == 1 and s[b]!=s[int(len(s)/2+b)]:
        a = 0
if a == 1:
    print("Yes")
else:
    print("No")
