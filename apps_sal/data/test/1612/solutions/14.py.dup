p = [set(list(map(int, input().split()))[1:]) for i in range(int(input()))]
for i, s in enumerate(p):
    print('YES' if all(i == i2 or not s2 <= s for i2, s2 in enumerate(p)) else 'NO')
