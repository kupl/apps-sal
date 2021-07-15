def main():
    n = int(input())
    Handels = []
    for i in range(n):
        rdl = input().split()
        if not rdl[0] in Handels:
            Handels.append(rdl[0])
            Handels.append(rdl[1])
        else: 
            ind = Handels.index(rdl[0])
            Handels[ind] = rdl[1]
    i = 0
    print(int(len(Handels)/2))
    while i < len(Handels):
        print(Handels[i], Handels[i+1])
        i +=2
main()
