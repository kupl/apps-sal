def main():
    n = int(input())
    s = input()
    fr = None
    sc = None
    ans = 0
    for elem in s:
        if fr == None:
            fr = elem
            ans += 1
        elif sc == None:
            if elem == fr:
                continue
            elif fr == 'L' and elem == 'R' or (fr == 'R' and elem == 'L') or (fr == 'D' and elem == 'U') or (fr == 'U' and elem == 'D'):
                ans += 1
                fr = elem
                sc = None
            else:
                sc = elem
        elif elem == fr or elem == sc:
            continue
        else:
            ans += 1
            fr = elem
            sc = None
    print(ans)


main()
