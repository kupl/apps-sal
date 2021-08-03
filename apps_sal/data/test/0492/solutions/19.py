s, e = input().split()
n = int(input())
n %= 4
if(n == 2 or n == 0):
    print("undefined")
elif(n == 1):
    if((s == '<' and e == '^') or (s == '^' and e == '>') or (s == '>' and e == 'v') or (s == 'v' and e == '<')):
        print("cw")
    else:
        print("ccw")
else:
    if((s == '<' and e == 'v') or (s == '^' and e == '<') or (s == '>' and e == '^') or (s == 'v' and e == '>')):
        print("cw")
    else:
        print("ccw")
