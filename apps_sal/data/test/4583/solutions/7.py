n=input()

for i in range(2 ** 3):
    

    co=["-","-","-"]

    for j in range(3):
        if ((i>>j)&1):
            co[2-j]="+"

    eq=n[0]+co[0]+n[1]+co[1]+n[2]+co[2]+n[3]


    if eval(eq)==7:
            ans=eq

print(ans,end="")
print("=7")

