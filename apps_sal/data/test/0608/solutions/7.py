n = input()
print(''.join(['.' if i > 3 else ' ' for i in map(int, input().split())]).count('...'))
