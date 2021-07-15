n, v = list(map(int, input().split()))
a = list(map(int, input().split()))

print('YES' if sum(a) - max(a) <= v else 'NO')

