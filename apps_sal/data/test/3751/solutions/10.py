import sys
3


def main():
    has = [False] * 26
    first = [-1] * 26
    cnt = 0
    s = input().strip()
    for i in range(len(s)):
        num = ord(s[i]) - ord('a')
        if not has[num]:
            has[num] = True
            first[num] = i
            cnt += 1
    for i in range(cnt):
        if not has[i]:
            print('NO')
            return
    for i in range(cnt, 26):
        if has[i]:
            print('NO')
            return
    for i in range(1, cnt):
        if first[i - 1] > first[i]:
            print('NO')
            return
    print('YES')


main()
