n = int(input())
x = set(map(int, input().split()[1:]))
y = set(map(int, input().split()[1:]))
for i in range(1, n + 1):
    if i not in x and i not in y:
        print('Oh, my keyboard!')
        break
else:
    print('I become the guy.')
