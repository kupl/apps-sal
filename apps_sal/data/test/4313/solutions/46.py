n = int(input())
*v, = map(int, input().split())
*c, = map(int, input().split())
s = [v[i] - c[i] for i in range(n)]
print(sum(i for i in s if i > 0))
