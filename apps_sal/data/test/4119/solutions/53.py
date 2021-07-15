n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

s = sorted([x[i]-x[i-1] for i in range(1, m)], reverse=True)
print(sum(s[n-1:]))
