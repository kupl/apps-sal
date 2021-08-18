s = list(map(int, input().split()))
s = [s[i:i + 2] for i in range(0, 8, 2)]
s.sort()
t = list(map(int, input().split()))
t = [t[i:i + 2] for i in range(0, 8, 2)]
t.sort()
for i in t:
    if s[0][0] <= i[0] <= s[3][0] and s[0][1] <= i[1] <= s[3][1]:
        print('YES')
        return
for i in s:
    if sum(t[0]) <= sum(i) <= sum(t[3]) and t[0][0] - t[0][1] <= i[0] - i[1] <= t[3][0] - t[3][1]:
        print('YES')
        return
O = [(t[0][0] + t[3][0]) // 2, (t[0][1] + t[3][1]) // 2]
if s[0][0] <= O[0] <= s[3][0] and s[0][1] <= O[1] <= s[3][1]:
    print('YES')
    return
print('NO')
