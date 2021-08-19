abc = list(map(int, input().split()))
print('YES' if abc.count(5) == 2 and abc.count(7) == 1 else 'NO')
