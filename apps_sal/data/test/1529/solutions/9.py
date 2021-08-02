n = int(input())
for i in range(0, n):
    s = input()
    ns = len(s)
    if ns < 5:
        print("OMG>.< I don't know!")
    else:
        if s[:5] == "miao." and s[-5:] == "lala.":
            print("OMG>.< I don't know!")
        else:
            if s[:5] == "miao.":
                print("Rainbow's")
            else:
                if s[-5:] == "lala.":
                    print("Freda's")
                else:
                    print("OMG>.< I don't know!")
