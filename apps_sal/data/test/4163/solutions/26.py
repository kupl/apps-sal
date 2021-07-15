N = int(input())

dices = [list(map(int, input().split())) for _ in range(N)]
dices = ''.join(list([str(int(x[0] == x[1])) for x in dices]))

print(('Yes' if '111' in dices else 'No'))


