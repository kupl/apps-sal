n = int(input())
snacks = map(int, input().split())
fall = [0] * (n + 1)
for snack in snacks:
    fall[snack] = 1
    output = []
    while fall[n] == 1:
        output.append(n)
        n -= 1
    print(' '.join(map(str, output)))
