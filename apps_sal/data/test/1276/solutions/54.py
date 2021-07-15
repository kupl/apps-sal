def main() -> None:
    n = int(input())
    s = input()

    answer = s.count('R') * s.count('G') * s.count('B')
    for i in range(n-2):
        for j in range(i+1, n-1):
            k = 2*j - i
            if k<n and s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
                answer -= 1
    print(answer)
    return


def __starting_point():
    main()

__starting_point()
