n = int(input())
for i in range(n):
    s = input()
    if s[len(s) - 5:len(s)] == 'lala.' and s[:5] == 'miao.':
        print("OMG>.< I don't know!")
    elif s[len(s) - 5:len(s)] == 'lala.':
        print("Freda's")
    elif s[:5] == 'miao.':
        print("Rainbow's")
    else:
        print("OMG>.< I don't know!")
