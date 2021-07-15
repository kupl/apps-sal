n = int(input())
a = list(map(int, input().split(" ")))

minus_odd = -10001
plus_odd = 10001
total = 0

for i in a:
    if i % 2:
        if i < 0:
            minus_odd = max(minus_odd, i)
        else:
            plus_odd = min(plus_odd, i)

    if i > 0:
        total += i

if total % 2 == 0:
    if minus_odd == -10001:
        print(total - plus_odd)
    elif plus_odd == 10001:
        print(total + minus_odd)
    else:
        if -minus_odd > plus_odd:
            print(total - plus_odd)
        else:
            print(total + minus_odd)

else:
    print(total)
