n = int(input())

s = input().split()

for i in range(n):
    s[i] = int(s[i])

m = int(input())
if(n == 1):
    for i in range(m):
        x = input()
    if(m == 0):
        print(s[0])
    else:
        print(0)

else:
    for i in range(m):
        x, y = list(map(int, input().split()))
        x -= 1
        if(x == 0):
            s[x] -= (y)
            s[x + 1] += s[x]
            s[x] = 0
        elif(x == n - 1):
            s[x] -= (s[x] - y) + 1
            s[x - 1] += s[x]
            s[x] = 0
        else:
            s[x - 1] += y - 1
            s[x] -= y
            s[x + 1] += s[x]
            s[x] = 0

    for item in s:
        print(item)
