n = int(input())

for i in range(0, n):
    s = input()
    if(s.startswith("miao.") and not s.endswith("lala.")):
        print("Rainbow's")
    elif(s.endswith("lala.") and not s.startswith("miao.")):
        print("Freda's")
    else:
        print("OMG>.< I don't know!")
