def f(str):
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True


s = input()
k = int(input())
if len(s) % k != 0:
    print('NO')
else:
    ans = True
    count = len(s) // k
    for i in range(k):
        ans = ans and f(s[i * count:(i + 1) * count])
    print('YES' if ans else 'NO')
