def main():
    t = int(input())
    for i in range(t):
        s = input()
        c = 0
        idx = []
        for j in range(len(s)):
            if(s[j] == "o"):
                if(j > 1) and (j < len(s) - 2):
                    if(s[j - 2:j] == "tw") and (s[j + 1:j + 3] == "ne"):
                        idx.append(j + 1)
                        c += 1
                    elif(s[j + 1:j + 3] == "ne"):
                        idx.append(j + 2)
                        c += 1
                    elif(s[j - 2:j] == "tw"):
                        idx.append(j)
                        c += 1
                elif(j < len(s) - 2):
                    if(s[j + 1:j + 3] == "ne"):
                        idx.append(j + 2)
                        c += 1
                elif(j > 1):
                    if(s[j - 2:j] == "tw"):
                        idx.append(j)
                        c += 1
        print(c)
        for j in range(len(idx)):
            if(j != len(idx) - 1):
                print(idx[j], end=" ")
            else:
                print(idx[j])


main()
