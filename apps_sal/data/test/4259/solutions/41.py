k = int(input())
a, b = map(int, input().split())
res = b//k
if a<=res*k:
    print("OK")
else:
    print("NG")
