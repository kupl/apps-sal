n = int(input())
if n == 1:
    a = input()
    print(a)
else:
    a = list(map(int, input().split()))
    b = [abs(i) for i in a]
    if min(a) * max(a) > 0:
        print(sum(b) - 2 * min(b))
    else:
        print(sum(b))
