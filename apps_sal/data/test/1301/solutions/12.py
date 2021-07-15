def __starting_point():
    names = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    N = int(input())
    nm = input()
    for x in names:
        if len(x) == N:
            st = True
            for i in range(N):
                if (nm[i]!='.') and (nm[i]!=x[i]):
                    st = False
            if st:
                print(x)
                break
                

__starting_point()
