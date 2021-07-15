n = int(input())
a = list(map(int, input().split()))
c = 0
t = False
for i in range(len(a)):
    if a[i] == i:
        c += 1
    else:
        if a[a[i]] == i and t == False:
            t = True
if n == c or n - 1 == c:
    print(c)
    return
if t == True:
    print(c + 2)
else:
    print(c + 1)

