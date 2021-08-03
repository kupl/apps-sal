n = int(input())
x, y = map(int, input().split())
val1 = max(x, y) - 1
val2 = n - min(x, y)
if(val1 <= val2):
    print('White')
else:
    print('Black')
