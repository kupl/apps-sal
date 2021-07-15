
t = int(input())
for qi in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print("Second")
    else:
        a.sort()
        f = True
        for i in range(0, n, 2):
            if a[i] != a[i+1]:
                f = False
                print("First")
                break
        if f:
            print("Second")
                

