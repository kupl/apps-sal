from sys import stdin, stdout

def main():
    s = input()
    p = sum([x == 'o' for x in s])
    l = sum([x == '-' for x in s])

    if p == 0 or l % p == 0:
        print('YES')
    else:
        print('NO')




main()

