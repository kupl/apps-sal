k = int(input())
a, b = (int(i) for i in input().split())

if b // k > (a - 1) // k:
    print("OK")
else:
    print("NG")
