def main():
    S = input()
    r_max = 0
    r = 0
    for i in range(len(S)):
        if S[i] == 'R':
            r += 1
            r_max = max([r, r_max])
        else:
            r = 0
    print(r_max)


main()
