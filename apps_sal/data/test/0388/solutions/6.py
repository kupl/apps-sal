def get(x):
    return chr(ord('A') + x // 26) + chr(ord('a') + x % 26)


def read(): return map(int, input().split())


n, k = read()
a = input().split()
ans = [0] * n
num = 1
for i in range(k - 1):
    ans[i] = num
    num += 1
for i in range(k - 1, n):
    cur = a[i - k + 1]
    if cur == 'YES':
        num += 1
        ans[i] = num
    else:
        ans[i] = ans[i - k + 1]
res = ' '.join(map(str, [get(i) for i in ans]))
print(res)
