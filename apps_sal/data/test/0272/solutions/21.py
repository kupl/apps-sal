def main():
    a = input()
    b = input()
    keyboard = dict()
    for i in range(ord('a'), ord('z') + 1):
        keyboard[chr(i)] = ' '
    index = 1
    size = 0
    out = ''
    size = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if keyboard[a[i]] == ' ' and keyboard[b[i]] == ' ':
                keyboard[a[i]] = b[i]
                keyboard[b[i]] = a[i]
                size += 1
                out += a[i] + ' ' + b[i] + '\n'
            elif not (keyboard[a[i]] == b[i] and keyboard[b[i]] == a[i]):
                print(-1)
                return 0
        elif keyboard[a[i]] == ' ':
            keyboard[a[i]] = a[i]
        elif keyboard[a[i]] != a[i]:
            print(-1)
            return 0
    print(size)
    if size > 0:
        print(out)


main()
