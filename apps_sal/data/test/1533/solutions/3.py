n = int(input())
s = set()
for i in range(n):
    sl = input()
    if sl not in s:
        print('NO')
    else:
        print('YES')
    s.add(sl)
