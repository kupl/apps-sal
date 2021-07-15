def main():
    s = input()
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    for c in s:
        if c == 'a':
            if cnt_b != 0 or cnt_c != 0:
                print('NO')
                return
            cnt_a += 1
        if c == 'b':
            if cnt_c != 0:
                print('NO')
                return
            cnt_b += 1
        if c == 'c':
            cnt_c += 1
    if cnt_a != 0 and cnt_b != 0 and (cnt_c == cnt_a or cnt_c == cnt_b):
        print('YES')
        return
    print('NO')


main()
