state = input("")
if(int(state) > 0):
    print(state)
elif(int(state) >= -10):
    print(0)
else:
    a = state[:-2] + state[-1]
    b = state[:-2] + state[-2]
    if(int(a) > int(b)):
        if(int(a) == 0):
            print(0)
        else:
            print(a)
    else:
        if(int(b) == 0):
            print(0)
        else:
            print(b)
