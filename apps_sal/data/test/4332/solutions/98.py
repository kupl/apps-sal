n = input()
l = len(n)

cnt = 0
for i in range(l):
    cnt += int(n[i])
n = int(n)
if n%cnt==0:
    print("Yes")
else:
    print("No")
