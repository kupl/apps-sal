cases = int(input())
for case in range(cases):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    if b > a * 2:
        print("NO")
    elif (a + b) % 3 == 0:
        print("YES")
    else:
        print("NO")
