

def main():
    n = int(input())
    s = set()
    for i in range(n):
        name = input()
        if name in s:
            print("YES")
        else:
            print("NO")
        s.add(name)
    

def __starting_point():
    main()
__starting_point()
