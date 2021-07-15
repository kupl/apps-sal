def main():
    n = int(input())
    s = set(input().split(" "))

    print("Four" if len(s) == 4 else "Three")


main()
