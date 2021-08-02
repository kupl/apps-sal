def mi():
    return list(map(int, input().split(' ')))


n, m = mi()
s = input()
ans = 1000000
for i in range(m):
    ans = min(ans, s.count(chr(65 + i)))

print(ans * m)
