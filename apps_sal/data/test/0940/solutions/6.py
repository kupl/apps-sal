USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    a = sorted(map(int, input().split(' ')))
    x = a[0] + a[1] - a[2]
    if x > 0:
        print(0)
    else:
        print(- x + 1)

def __starting_point():
    main()




__starting_point()
