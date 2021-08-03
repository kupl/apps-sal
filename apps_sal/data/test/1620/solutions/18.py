n = int(input())
currs = 0
while(n > 1):
    n -= 2
    if(currs == 0):
        print("aa", end="")
        currs = 1
    else:
        print("bb", end="")
        currs = 0
if(n == 1):
    if(currs == 0):
        print("a", end="")
    else:
        print("b", end="")
