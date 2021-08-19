def main():
    tok = input().split()
    A = int(tok[0])
    B = int(tok[1])
    ans = 0
    for a in range(1, 70):
        for b in range(70):
            num = (2 ** a - 1) * 2 ** (b + 1) + (2 ** b - 1)
            if num >= A and num <= B:
                ans += 1
    print(ans)


main()
