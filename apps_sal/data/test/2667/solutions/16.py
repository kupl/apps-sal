# cook your dish here
l = []
n = int(input())
x = map(int, input().split())
x1 = sum(x)
for i in range(1, n + 1):
    l.append(i)

l1 = sum(l)
if x1 == l1:
    print("YES")
else:
    print("NO")
