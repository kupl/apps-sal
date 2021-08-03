n = int(input())


def solve(i, n):
    s = "I love" if i % 2 == 0 else "I hate"

    if i == n:
        return s + " it"
    else:
        return s + " that " + solve(i + 1, n)


print(solve(1, n))
