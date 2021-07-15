3

n, m = input().split()
n = int(n)
m = int(m)

if n == m == 1:
    print("YES")
else:
    x, y = input(), input()
    x = (1 if x[0] == '<' else 0, 1 if x[-1] == '>' else 0)
    y = (1 if y[0] == 'v' else 0, 1 if y[-1] == '^' else 0)
    if (sum(x) + sum(y)) % 4 == 0:
        print("YES")
    else:
        print("NO")

