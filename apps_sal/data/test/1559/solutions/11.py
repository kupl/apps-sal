L = int(input())
string = input()

length = len(string)
if length % L != 0:
    print(('1'+'0'*(L-1))*((length + L -1)//L))
else:
    uptoL = string[:L]
    periodic = uptoL * (length//L)

    if periodic > string:
        print(periodic)
    elif uptoL.count('9') == L:
        print(('1'+'0'*(L-1))*((length + L )//L))
    else:
        print(str(int(uptoL)+1)*(length//L))

