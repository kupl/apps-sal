'''
def main():
    from sys import stdin,stdout
def __starting_point():
    main()
'''
#10/9/22016-370.2
#2
def main():
    from sys import stdin,stdout
    s=stdin.readline().strip().lower()
    if len(s) & 1:
        stdout.write('-1')
    else:
        x=0
        y=0
        for i in s:
            if i=='l':
                x-=1
            elif i=='r':
                x+=1
            elif i=='u':
                y+=1
            elif i=='d':
                y-=1
        stdout.write(str((abs(x)+abs(y))//2))
            
def __starting_point():
    main()

__starting_point()
