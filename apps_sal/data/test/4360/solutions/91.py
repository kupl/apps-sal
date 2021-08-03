N = int(input())
A = map(int, input().split())
print('{:.16g}'.format(1 / sum(1 / x for x in A)))
