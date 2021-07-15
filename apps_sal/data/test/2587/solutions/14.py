n=int(input())
for i in range(n):
    t=int(input())
    r=(3*t)//4
    string = ""
    for j in range(r):
        string+="9"
    for j in range(t-r):
        string+="8"
    string+="\n"
    print(string,end="")
