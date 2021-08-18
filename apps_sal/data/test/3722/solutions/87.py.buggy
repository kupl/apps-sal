import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()


N = I()
AA, AB, BA, BB = S(), S(), S(), S()
mod = 10**9 + 7

if N <= 3:
    print((1))
    return

ans1 = 1

fib = [1, 1]
for i in range(N - 3):
    fib.append((fib[-1] + fib[-2]) % mod)
ans2 = fib[-1]

ans3 = pow(2, N - 3, mod)


if AB == 'A':
    if AA == 'A':
        ans = ans1
    else:
        if BA == 'A':
            ans = ans2
        else:
            ans = ans3
else:
    if BB == 'B':
        ans = ans1
    else:
        if BA == 'B':
            ans = ans2
        else:
            ans = ans3

print(ans)
