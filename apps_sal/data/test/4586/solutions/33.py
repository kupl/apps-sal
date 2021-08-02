def main():
    x = input()

    if len(set(x[:3])) == 1 or len(set(x[1:])) == 1:
        print("Yes")
    else:
        print("No")


main()
