from sys import stdin
def main():
        n=int(stdin.readline())
        ville=stdin.readline()
        minimum=n
        maisons={}
        nbType=0
        for maison in ville:
                if maison!="\n" and maison not in maisons:
                        maisons[maison]=0
                        nbType+=1
        nbZeros=nbType-1
        inf=0
        sup=0
        maisons[ville[0]]+=1
        while n>sup:
                if nbZeros==0:
                        minimum=min(minimum,sup-inf+1)
                        maisons[ville[inf]]-=1
                        if maisons[ville[inf]]==0:
                                nbZeros+=1
                        inf+=1

                else:
                        sup+=1
                        if n>sup:
                                maisons[ville[sup]]+=1
                                if maisons[ville[sup]]==1:
                                        nbZeros-=1
        print(minimum)
main()

