n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        tmp = a
        a = b
        b = tmp
    
    if b > 2 * a:
        print("NO")
    else:
        if (a + b) % 3 == 0:
            print("YES")
        else:
            print("NO")
