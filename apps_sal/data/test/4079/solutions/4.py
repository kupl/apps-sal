GI = lambda: int(input()); GIS = lambda: list(map(int, input().split())); LGIS = lambda: list(GIS())

def main():
    for t in range(GI()):
        s = sorted(input())
        for i in range(len(s) - 1):
            if ord(s[i+1]) - ord(s[i]) != 1:
                print("No")
                break
        else:
            print("Yes")

main()

