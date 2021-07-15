n, k = map(int, input().split())
s = input()
if k - 1 == 0:
    for i in range(n - 1):
        print("PRINT", s[i])
        print("RIGHT")
    print("PRINT", s[-1])
elif k == n:
    for i in range(n - 1, 0, -1):
        print("PRINT", s[i])
        print("LEFT")
    print("PRINT", s[0])
elif n - k + 1 <= k - 1:
    for i in range(k, n):
        print("RIGHT")
    for i in range(n - 1, 0, -1):
        print("PRINT", s[i])
        print("LEFT")
    print("PRINT", s[0])
else:
    for i in range(k - 1, 0, -1):
        print("LEFT")
    for i in range(n - 1):
        print("PRINT", s[i])
        print("RIGHT")
    print("PRINT", s[-1])    
