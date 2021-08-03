def main():
    n = int(input())
    s = input()
    for c in s:
        if c == 'Y':
            print('Four')
            return
    print('Three')


main()
