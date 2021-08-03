n = 0
m = 0


def esht(a, b):

    nonlocal n, m

    for ptr in range(0, len(a)):
        if (a[ptr] is '#') and (a[ptr] == b[ptr]):
            return True
    return False


def main():
    nonlocal n, m
    n, m = [*list(map(int, input().split()))]
    s = ["" for i in range(0, n)]
    for i in range(0, n):
        s[i] = input()
    ans = True
    for i in range(0, n):
        for j in range(i + 1, n):
            if esht(s[i], s[j]) and s[i] != s[j]:
                ans = False
    if ans is True:
        print("Yes")
    else:
        print("No")


main()
