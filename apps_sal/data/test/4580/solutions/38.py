N = int(input())
a = list(map(int, input().split()))
rate = set()
over = 0
for ai in a:
    if ai >= 3200:
        over += 1
    else:
        rate.add(ai // 400)
L = len(rate)
print(max(1, L), L + over)
