n = int(input())
a = list(map(int,input().split()))
b = len(set(a))
if n == b:
    print("YES")
else:
    print("NO")
