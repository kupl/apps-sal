def main():
    s = input()
    ans = 'no'
    if len(set(s)) == len(s):
        ans = 'yes'
    print(ans)



def __starting_point():
    main()

__starting_point()
