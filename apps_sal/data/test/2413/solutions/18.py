def solve(a):
    left0 = 0
    right0 = 0
    if '1' not in a:
        return len(a)
    for i in a:
        if i == '0':
            left0 += 1
        else:
            break
    for i in a[::-1]:
        if i == '0':
            right0 += 1
        else:
            break
    return len(a) * 2 - min(left0, right0) * 2


def main():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        a = input()
        print(solve(a))


main()

