t = int(input())
while t:
    s = input()
    ls = []
    for i in range(len(s)):
        if(s[i] == "1"):
            ls.append(i)
    if(len(ls) == 0):
        print(0)
    else:
        count = 0
        for i in range(ls[0], ls[-1]):
            if(s[i] == "0"):
                count += 1
        print(count)
    t -= 1
