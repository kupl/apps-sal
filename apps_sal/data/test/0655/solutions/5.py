n = int(input())
x, y = list(map(int, input().split()))
num = x - 1 + y - 1
num2 = n - x + n - y
ans = num <= num2
if ans:
    print("White")
else:
    print("Black")
