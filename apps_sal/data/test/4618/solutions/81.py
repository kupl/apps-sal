def main():
    s=input()
    k=int(input())
    a=set()
    for l in range(5):
        for i in range(len(s)-l):
            a.add(s[i:i+l+1])
    print(sorted(a)[k-1])

def __starting_point():
    main()
__starting_point()
