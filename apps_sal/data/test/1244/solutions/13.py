n = int(input())
a = input().split()
print('YES' if all((a.count(i) * 2 - 1 <= n for i in a)) else 'NO')
