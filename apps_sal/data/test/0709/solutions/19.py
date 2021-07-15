def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")

    if mode=="file":n=int(f.readline())
    else:n=int(input())
    print(sum( (n>>shift)&1 for shift in range(128) ))


    if mode=="file":f.close()


def __starting_point():
    main()

__starting_point()
