USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    n, = list(map(int, input().split(' ')))
    print(n.bit_length())

def __starting_point():
    main()




__starting_point()
