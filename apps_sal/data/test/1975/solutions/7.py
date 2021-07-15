
def main():
        nm=input().split(" ")
        n=int(nm[0])
        m=int(nm[1])
        nos=0
        pairs=[]
        for i in range(1):
                for j in range(m):
                        pairs.append([i+1,j+1]);
                        nos+=1
        for j in range(1,n):
                pairs.append([j+1,1])
                nos+=1
        print (nos)
        for i in pairs:
                pair=str(i[0])+" "+str(i[1])
                print (pair)
def __starting_point(): main()


__starting_point()
