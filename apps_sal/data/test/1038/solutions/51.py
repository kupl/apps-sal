A,B = map(int,input().split())
l = B - A + 1
if A % 2 == 0:
    if l % 2 == 0:
        if l % 4 == 0:
            ans = 0
        else:
            ans = 1
    elif (l-1) % 4 == 0:
        ans = B
    else:
        ans = B^1
else:
    if l % 2 == 0:
        if (l-2) % 4 == 0:
            ans = A^B
        else:
            ans = A^B^1
    elif (l-1) % 4 == 0:
        ans = A
    else:
        ans = A^1
if A == B:
    ans = A

print(ans)
