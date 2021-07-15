def main():
    n = int(input())
    lines = []
    d = {}
    for _ in range(n):
        l = input()
        if l not in d:
            d[l] = 0
        d[l] +=1
    ans = max(d.values())
    print(ans)

def __starting_point():
    main()
    

__starting_point()
