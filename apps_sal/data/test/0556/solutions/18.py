a, b, c = map(int, input().split())

val = 1
flag = 0

while val <= b:
    if val >= a:
        flag = 1
        print(val, end=" ")
    val = val * c

if flag == 0:
    print(-1)
