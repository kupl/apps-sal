def main():
    n = input()
    print("".join("9" if s=="1" else "1" for s in n))


main()
