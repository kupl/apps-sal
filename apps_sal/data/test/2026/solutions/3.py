def main():
    n = int(input())
    s = input()
    fr = None
    sc = None
    ans = 0 
    for elem in s:
        if (fr == None):
            fr = elem
            ans += 1
        else:
            if (sc == None):
                if (elem == fr):
                    continue
                else:
                    if (fr == 'L' and elem == 'R') or (fr == 'R' and elem == 'L') or (fr == 'D' and elem == 'U') or (fr == 'U' and elem == 'D'): 
                        ans += 1
                        fr = elem
                        sc = None
                    else:
                        sc = elem
            else:
                if (elem == fr or elem == sc):
                    continue
                else:
                    ans += 1
                    fr = elem
                    sc = None
    print(ans)
main()

