input()
a = list(map(int, input().split()))
print('YES' if len(a) == 1 and sum(a) == 1 or (len(a) != 1 and sum(a) == len(a) - 1) else 'NO')
