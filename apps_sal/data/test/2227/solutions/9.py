def main():
    s = str(input())
    s = s.replace('heavy', '-')
    s = s.replace('metal', '+')
    (p, n) = (0, 0)
    for k in s:
        if k == '-':
            n += 1
        elif k == '+':
            p += n
    print(p)


main()
