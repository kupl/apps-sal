def ans1(n, k, s):
    ans = []
    for i in range(k - 1, n - 1):
        ans.append("PRINT " + s[i])
        ans.append("RIGHT")
    ans.append("PRINT " + s[n - 1])
    for i in range(k, n + 1):
        ans.append("LEFT")
    for i in range(k - 2, 0, -1):
        ans.append("PRINT " + s[i])
        ans.append("LEFT")
    ans.append("PRINT " + s[0])
    return ans


def ans2(n, k, s):
    ans = []
    for i in range(k - 1, 0, -1):
        ans.append("PRINT " + s[i])
        ans.append("LEFT")
    ans.append("PRINT " + s[0])
    for i in range(k):
        ans.append("RIGHT")
    for i in range(k, n - 1):
        ans.append("PRINT " + s[i])
        ans.append("RIGHT")
    ans.append("PRINT " + s[n - 1])
    return ans


def main():
    n, k = map(int, input().split())
    s = input()
    if n == k:
        for i in range(n - 1, 0, -1):
            print("PRINT", s[i])
            print("LEFT")
        print("PRINT", s[0])
    elif k == 1:
        for i in range(n - 1):
            print("PRINT", s[i])
            print("RIGHT")
        print("PRINT", s[n - 1])
    else:
        a1 = ans1(n, k, s)
        a2 = ans2(n, k, s)
        if len(a1) < len(a2):
            for line in a1:
                print(line)
        else:
            for line in a2:
                print(line)


main()
