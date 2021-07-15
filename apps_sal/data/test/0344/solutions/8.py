def main():
    a = input().strip()
    vowel = 'aeiou'
    if a[-1] not in vowel and a[-1]!='n':
        print('NO')
        return
    for i in range(len(a)-1):
        if a[i] not in vowel:
            if a[i]!='n':
                if a[i+1] not in vowel:
                    print('NO')
                    return
    print('YES')
    return
def __starting_point():
    main()


__starting_point()
