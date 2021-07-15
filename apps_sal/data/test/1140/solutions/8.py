tcs = int(input())
b = list(map(int, input().split(' ')))
up = max(b)
down = min(b)
if up != down:
    diff = abs(up-down)
    ctmx = b.count(up)
    ctmn = b.count(down)
    print(diff, ctmx*ctmn)
else:
    print(0, int(tcs*(tcs-1)/2))

