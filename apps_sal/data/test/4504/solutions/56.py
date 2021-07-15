import sys

input = sys.stdin.readline

def main():
    ans = 0
    s = input().rstrip('\n')
    ls = len(s)
    for i in range(1,ls):
        if (ls - i)%2 != 0:
            continue
        temps = s[:-i]
        if temps[:(ls-i)//2] == temps[(ls-i)//2:]:
            ans = ls - i 
            break

    print(ans)

def __starting_point():
    main()
__starting_point()
