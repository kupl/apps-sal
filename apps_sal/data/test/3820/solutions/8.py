(n, m) = list(map(int, input().split()))
s = input()
t = input()
if '*' not in s:
    if s == t:
        print('YES')
    else:
        print('NO')
else:
    a = s.split('*')
    if len(t) >= len(s) - 1 and t[:len(a[0])] == a[0] and (len(a[1]) == 0 or t[-len(a[1]):] == a[1]):
        print('YES')
    else:
        print('NO')
