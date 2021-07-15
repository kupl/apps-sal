def main():
    name = input()
    s = ('B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'Z')
    for ch in s:
        if ch in name:
            print('NO')
            return
    if name[:len(name) // 2] != name[::-1][:len(name) // 2]:
        print('NO')
        return
    print('YES')

main()

