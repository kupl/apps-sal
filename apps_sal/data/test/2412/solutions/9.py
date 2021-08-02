t = int(input())
for l in range(t):
    n = int(input())
    s = str(input())
    flag = 0
    for i in range(n):
        if(s[i] == '8'):
            if(n - i >= 11):
                flag = 1
                break
    if(flag == 1):
        print("YES")
    else:
        print("NO")
