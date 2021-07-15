n = int(input())
a = [int(s) for s in input().split()]

print('YES') if len(a) == len(set(a)) else print('NO')
