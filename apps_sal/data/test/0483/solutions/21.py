def main():
    n = input()
    s = input()
    d = input()
    number = []
    res = False
    maxi = float('inf')
    for i in d.split(" "):
        number.append(int(i))
    for i in range(len(s) - 1):
        if ( s[i] == "R" and s[i + 1] == "L" ):
            cal = number[i+1] - number[i]
            if (cal < maxi):
                maxi = cal
            res = True
    
    if (res == True):
        maxi = int(maxi/2)
        print(maxi)
    else:
        print("-1")

main()

