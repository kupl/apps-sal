n=int(input())
for x in range(n):
    s=input()
    l=len(s)
    if(len(s)>=2 and s[l-2:l]=="po"):
        print("FILIPINO")
    if(len(s)>=4 and s[l-4:l]=="desu"):
        print("JAPANESE")
    if(len(s)>=4 and s[l-4:l]=="masu"):
        print("JAPANESE")
    if(len(s)>=5 and s[l-5:l]=="mnida"):
        print("KOREAN")

