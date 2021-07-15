n = int(input())

nochange = True
order_kept = True

prev_b = float("inf")
for i in range(n):
    b, a = list(map(int, input().split()))
    if b != a:
        nochange = False
        break
    if b > prev_b:
        order_kept = False
    prev_b = b

if not nochange:
    print("rated")
else:
    if order_kept:
        print("maybe")
    else:
        print("unrated")

