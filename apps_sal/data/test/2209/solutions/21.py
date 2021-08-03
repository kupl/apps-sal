def key(x):
    try:
        return x.count('h') / x.count('s')
    except ZeroDivisionError:
        return 10**9


n = int(input())
t = ''.join(sorted((input() for _ in range(n)), key=key))

res, cnt = 0, 0
for ti in t:
    if ti == 's':
        cnt += 1
    if ti == 'h':
        res += cnt
print(res)
