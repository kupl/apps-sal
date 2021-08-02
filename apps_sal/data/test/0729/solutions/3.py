n = int(input())
s = input()
if(n == 1):
    print("NO")
else:
    for x in range(n - 1):
        a, b = s[x], s[x + 1]
        if(a != b):
            print("YES")
            print(a + b)
            break
    else:
        print("NO")
