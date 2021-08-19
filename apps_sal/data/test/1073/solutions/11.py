def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        vert = horiz = 0
        for j in range(i, n):
            if s[j] == 'U':
                vert += 1
            elif s[j] == 'R':
                horiz += 1
            elif s[j] == 'D':
                vert -= 1
            else:
                horiz -= 1
            if vert == 0 and horiz == 0:
                cnt += 1
    print(cnt)


main()
