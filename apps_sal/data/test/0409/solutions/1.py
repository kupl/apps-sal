S = input()
if S.count("AB") == 0 or S.count("BA") == 0 :
    print("NO")
else :
    if S[S.index("AB")+2:].count("BA") > 0 or S[S.index("BA")+2:].count("AB") > 0 :
            print("YES")
    else :
        print("NO")

