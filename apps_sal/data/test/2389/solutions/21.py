def main():
    n, a, b, c = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    num = dict(A=a, B=b, C=c)
    t = a + b + c
    ans = []
    if t == 0:
        print("No")
        return
    if t == 1:
        for i in range(n):
            si = s[i]
            if num[si[0]] == 1:
                num[si[0]] -= 1
                num[si[1]] += 1
                ans.append(si[1])
            elif num[si[1]] == 1:
                num[si[0]] += 1
                num[si[1]] -= 1
                ans.append(si[0])
            else:
                print("No")
                return
        print("Yes")
        print("\n".join(ans))
        return
    for i in range(n - 1):
        si = s[i]
        if num[si[0]] == 0 and num[si[1]] >= 1:
            num[si[0]] += 1
            num[si[1]] -= 1
            ans.append(si[0])
        elif num[si[1]] == 0 and num[si[0]] >= 1:
            num[si[0]] -= 1
            num[si[1]] += 1
            ans.append(si[1])
        elif num[si[0]] >= 1 and num[si[1]] >= 1:
            sin = s[i + 1]
            if si[0] in sin:
                num[si[0]] += 1
                num[si[1]] -= 1
                ans.append(si[0])
            else:
                num[si[0]] -= 1
                num[si[1]] += 1
                ans.append(si[1])
        else:
            print("No")
            return
    if num[s[n - 1][0]] >= 1:
        ans.append(s[n - 1][1])
    elif num[s[n - 1][1]] >= 1:
        ans.append(s[n - 1][0])
    else:
        print("No")
        return
    print("Yes")
    print("\n".join(ans))
    return


def __starting_point():
    main()


__starting_point()
