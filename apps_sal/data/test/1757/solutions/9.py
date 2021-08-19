fib1 = 1
fib2 = 2
n = int(input())
ans = 'O'
for i in range(2, 1 + n):
    if i < fib2:
        ans += 'o'
    else:
        ans += 'O'
        (fib1, fib2) = (fib2, fib1 + fib2)
print(ans)
