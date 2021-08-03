n = int(input())
s = [int(i) for i in input().split()]
t = 0
for i in s:
    if i - t < 0:
        print("NO")
        break
    t = (i - t) % 2
else:
    if t:
        print("NO")
    else:
        print("YES")
