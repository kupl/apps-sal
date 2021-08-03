n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    n -= i
if(n >= 0):
    print(n)
else:
    print("-1")
