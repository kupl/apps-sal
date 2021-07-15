def main():
    s = input()
    letters = ''
    for i in range(26):
        letters += chr(i + ord('a'))
    marked = [False] * 26
    ind = 0
    for c in s:
        if marked[ord(c) - ord('a')]:
            continue
        if letters[ind] != c:
            print('NO')
            return
        marked[ind] = True
        ind += 1
    print('YES')

main()

