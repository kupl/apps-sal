def main():
    c1 = input()
    c2 = input()

    if all((c1[0] == c2[2], c1[2] == c2[0], c1[1] == c2[1])):
        print("YES")
    else:
        print("NO")


main()
