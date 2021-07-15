n = int(input())
x = [int(s) for s in input().split()]
y = [int(s) for s in input().split()]
s1 = 0
s2 = 0
for i in range(n):
    s1 += x[i]
    s2 += y[i]
if s2 > s1:
    print("No")
else:
    print("Yes")
