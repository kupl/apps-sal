(a, b) = map(int, input().split())
n = list(map(int, input().split()))
m = sorted(n)[::-1]
if a <= b:
    print('0')
else:
    print(sum(m[b:]))
