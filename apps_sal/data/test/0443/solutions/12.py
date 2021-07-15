n = int(input())
b = []
s = input().split()
for i in range(n):
    b.append((int(s[i]), i + 1))
if n == 1:
    print(-1)
elif n == 2:
    if b[0][0] == b[1][0]:
        print(-1)
    else:
        print(1)
        print(1)
else:
    b.sort()
    print(1)
    print(b[0][1])
