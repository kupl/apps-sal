n, k = list(map(int, input().split()))
s = input()
left = k - 1
right = n - k
if left > right:
    for i in range(n - k):
        print("RIGHT")
    for j in range(n - 1, 0, -1):
        print("PRINT " + s[j])
        print("LEFT")
    print("PRINT " + s[0])
else:
    for i in range(k - 1):
        print("LEFT")
    for j in range(n -1):
        print("PRINT " + s[j])
        print("RIGHT")
    print("PRINT " + s[n - 1])

