for _ in range(int(input())):
    n=int(input())
    s=input()
    if n==2 and int(s[0])>=int(s[1]):
        print("NO")
    else:
        print("YES",2,sep='\n')
        print(s[0],s[1:])
