def main():
    a = input()
    b = input()
    x = max(len(a), len(b))
    a = "0" * (x - len(a)) + a
    b = "0" * (x - len(b)) + b

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")


main()
