def main():
    s = input()
    t = input()
    x = len(s)

    for index in range(x):
        if (s[index+1:] + s[:index+1]) == t:
            print("Yes")
            return

    print("No")


main()
