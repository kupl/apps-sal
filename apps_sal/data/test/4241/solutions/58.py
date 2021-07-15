def main():
    S = input()
    T = input()
    size = len(T)
    count = 10000
    for i in range(len(S)-size+1):
        x = 0
        for j in range(size):
            if S[i+j] != T[j]:
                x+=1
        count = min(count,x)
    print(count)              

def __starting_point():
    main()


__starting_point()
