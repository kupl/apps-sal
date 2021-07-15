USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    n,  = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    a.sort()
    ans = a[-1] - a[0] + 1 - n
    print(ans)

def __starting_point():
    main()




__starting_point()
