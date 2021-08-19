(n, m, x) = map(int, input().split())
A = list(map(int, input().split()))
print(min(sum([a < x for a in A]), sum([a > x for a in A])))
