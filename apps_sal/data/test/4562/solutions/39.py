def main():
    N = int(input())
    a = 1
    i = 0
    prev = 0
    while a <= N:
        i += 1
        prev = a
        if a > N:
            break
        else:
            a = i * i
    print(prev)


main()
