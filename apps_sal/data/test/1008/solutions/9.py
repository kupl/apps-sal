def f(s, k):
    for j in range(k - k // 2):
        if s[j] != s[-(j + 1)]:
            return False
    else:
        return True


s = input()
k = int(input())
if len(s) % k != 0:
    print('NO')
else:
    k = len(s) // k
    for i in range(0, len(s), k):
        if not f(s[i:i + k], k):
            print('NO')
            break
    else:
        print('YES')
