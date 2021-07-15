from _collections import deque

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar = deque(ar)
    turn = 0
    a, b = 0, 0
    num2 = 0
    x = 0
    while ar:
        if turn == 0:
            num1 = 0
            while ar and num1 <= num2:
                num1 += ar[0]
                ar.popleft()
            a += num1
            num2 = num1
            turn = 1
        else:
            num1 = 0
            while ar and num1 <= num2:
                num1 += ar[-1]
                ar.pop()
            b += num1
            num2 = num1
            turn = 0
        x += 1
    print(x, a, b)
