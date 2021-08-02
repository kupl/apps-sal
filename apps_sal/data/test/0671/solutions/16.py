def main():
    n = int(input())
    s = ''
    ind = 1
    while len(s) < n:
        s += str(ind)
        ind += 1
    print(s[n - 1])


main()
