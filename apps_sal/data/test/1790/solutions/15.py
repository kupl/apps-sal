n = int(input())
s = set(map(int, input().split()[1:]))
for i in range(n - 1):
    s = s.intersection(map(int, input().split()[1:]))
print(' '.join(map(str, s)))
