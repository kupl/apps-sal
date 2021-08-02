n = int(input())
for i in range(n):
    s = input()
    ans = 0
    if s[-5:] == 'lala.':
        ans += 1
    if s[:5] == 'miao.':
        ans += 2
    if ans == 1:
        print("Freda's")
    elif ans == 2:
        print("Rainbow's")
    else:
        print("OMG>.< I don't know!")
