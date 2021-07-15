def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i:i+3] == 'ABC':
            cnt += 1
    return cnt
def __starting_point():
    print(main())
__starting_point()
