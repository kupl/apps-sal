a = int(input())
b, c = map(int, input().split())

x = c // a
if(x >= 1 and x * a >= b):
    print("OK")
else:
    print("NG")
