q = int(input())
for z in range(q):
    (a, b, c) = map(int, input().split())
    if a > b + c + 1 or b > a + c + 1 or c > a + b + 1:
        print('No')
    else:
        print('Yes')
