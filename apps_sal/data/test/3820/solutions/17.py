USE_STDIO = False

if not USE_STDIO:
    try: import mypc
    except: pass

def main():
    n, m = list(map(int, input().split(' ')))
    s = input()
    t = input()

    i = s.find('*')
    if i < 0: return s == t
    return len(t) >= len(s) - 1 and s[:i] == t[:i] and s[i+1:] == t[len(t)-len(s)+i+1:]

def __starting_point():
    print(['NO', 'YES'][main()])




__starting_point()
