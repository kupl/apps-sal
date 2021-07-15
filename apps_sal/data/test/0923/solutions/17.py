n = int(input())
l = [int(i) for i in input().split()]
d = (n - l[0]) % n
for i in range(1, n):
    r = n
    if i & 1 == 0:
        if i >= l[i]:
            r = i - l[i]
        else:
            r = i - l[i] + n
    else:
        if i <= l[i]:
            r = l[i] - i
        else:
            r = l[i] - i + n
    if r != d:
        print("No")
        d = -1
        break
if d >= 0:
    print("Yes")
    
    

