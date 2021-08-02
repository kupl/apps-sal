ans = []
for _ in range(int(input())):
    n = int(input())
    ansi = '9' * (3 * n // 4) + '8' * ((n - 1) // 4 + 1)
    ans.append(ansi)
print('\n'.join(ans))
