import sys
sys.setrecursionlimit(10**6)


a, b = list(map(str, input().split()))


num = int(a + b)

if num == int(num**0.5)**2:
    print("Yes")
else:
    print("No")
