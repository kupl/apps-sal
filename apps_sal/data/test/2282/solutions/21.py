def main():
    n = int(input())
    s = input()
    left = 0 - s.count('L')
    right = 0 + s.count('R')

    print(right - left + 1)


main()
