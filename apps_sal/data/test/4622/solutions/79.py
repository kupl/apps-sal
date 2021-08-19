n = int(input())
a = list(set(map(int, input().split())))
print('YES') if n == len(a) else print('NO')
