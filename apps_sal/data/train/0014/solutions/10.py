t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    if max(a, b) == max(c, d):
        if min(a, b) + min(c, d) == max(a, b):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
