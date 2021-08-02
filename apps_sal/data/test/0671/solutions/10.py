def main():
    n = int(input())
    s = "123456789"
    x = 10
    n -= 1
    while len(s) <= n:
        s += str(x)
        x += 1
    print(s[n])


main()
