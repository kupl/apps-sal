def f():
    n, x = list(map(int, input().split()))

    a = list(map(int, input().split()))

    odds = 0
    for i in a:
        if i % 2 == 1:
            odds += 1

    if odds == n:
        if x % 2 == 1:
            return "Yes"
        else:
            return "No"
    elif odds == 0:
        return "No"
    else:
        if x == n and odds % 2 == 0:
            return "No"
        else:
            return "Yes"

t = int(input())

for _ in range(t):
    print(f())

