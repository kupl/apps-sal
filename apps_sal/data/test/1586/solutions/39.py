N = int(input())
ans = 0
if N % 2 == 0:
    five = 10
    while N // five > 0:
        ans += N // five
        five *= 5
print(ans)
