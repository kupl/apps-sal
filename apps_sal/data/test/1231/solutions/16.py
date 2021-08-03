n, m = input().split()
n, m = int(n), int(m)
if(m + n != 0):

    if((m - n) == 1 or (m - n) == 0 or (m - n) == -1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
