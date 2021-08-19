import sys


def main():
    names = []
    for i in range(26):
        s = 'A' + chr(ord('a') + i)
        s1 = 'X' + chr(ord('a') + i)
        names.append(s)
        names.append(s1)
    (n, k) = map(int, sys.stdin.readline().split())
    r = list(sys.stdin.readline().split())
    res = ['Ho'] * n
    cur = 0
    firstYes = -1
    for i in range(n - k + 1):
        if r[i] == 'YES':
            firstYes = i
            break
    if firstYes == -1:
        print(' '.join(res))
        return
    for i in range(firstYes + 1, firstYes + k):
        res[i] = names[cur]
        cur += 1
    for i in range(firstYes + 1, n - k + 1):
        if r[i] == 'YES':
            res[i + k - 1] = names[cur]
            cur += 1
        else:
            res[i + k - 1] = res[i]
    print(' '.join(res))


main()
