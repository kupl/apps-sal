def main():
    s = input()
    t = input()
    i, j, m, l = 0, len(t) - 1, 0, len(s) - 1
    while i < j:
        if m != len(s):
            if t[i] == s[m]:
                m += 1 
            if m != len(s):
                i += 1
        if l != -1:
            if t[j] == s[l]:
                l -= 1
            if l != -1:
                j -= 1
        if m == len(s) and l == -1:
            print(j-i)
            break
    else:
        print(0)
        
def __starting_point():
    main()

__starting_point()
