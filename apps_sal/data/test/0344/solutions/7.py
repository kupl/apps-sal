def main():
    # string         input()
    # int            int(input())
    # listOfStrings  input().split()
    # ints           map(int, input().split())
    # listOfInts     list(map(int, input().split()))
    s = input()
    i = 0
    l = len(s)
    alpha = "bcdfghjklmpqrstvwxyz"
    vowels = "aeiou"
    if s[-1] in alpha:
        print("NO")
        return 0
    while i < l - 1:
        if s[i] in alpha:
            if s[i + 1] in vowels:
                i += 2
                while i < l and s[i] in vowels:
                    i += 1
            else:
                print("NO")
                return 0
        else:
            i += 1
    print("YES")
    return 0


main()
