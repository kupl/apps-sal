
def main():
    s = input()
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            print("No")
            return
    s1 = s[:(n-1)//2]
    s2 = s[(n+3)//2-1:]
    n1 = len(s1)
    for i in range(n//4):
        if s1[i] != s[n1-1-i]:
            print("No")
            return
        if s2[i] != s[n1-1-i]:
            print("No")
            return
    print("Yes")

def __starting_point():
    main()
__starting_point()
