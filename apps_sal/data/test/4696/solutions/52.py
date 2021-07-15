a, b = map(int, input().split())

flag = (a*b %2 ==0)
if flag:
    print("Even")
else:
    print("Odd")
