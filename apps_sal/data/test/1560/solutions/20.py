def main():
    n = int(input())
    s = input()
    rodd = 0
    bodd = 0
    reven = 0
    beven = 0
    for (i, c) in enumerate(s):
        if i % 2 == 1:
            if c == 'r':
                rodd += 1
            else:
                bodd += 1
        elif c == 'r':
            reven += 1
        else:
            beven += 1
    print(min(abs(bodd - reven) + min(bodd, reven), abs(rodd - beven) + min(rodd, beven)))


main()
