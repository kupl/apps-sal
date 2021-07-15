def main():
    s = input()
    start = 200000
    end = 0
    for i in range(len(s)):
        if s[i] == 'A' and start > i:
            start = i
        elif s[i] == 'Z' and end < i:
            end = i
    print(end - start + 1)



def __starting_point():
    main()
__starting_point()
