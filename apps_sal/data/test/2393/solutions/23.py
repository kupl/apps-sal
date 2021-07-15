for _ in range(int(input())):
    i = 0
    z = input()
    ans = []
    while i+2 < len(z):
        if z[i] == "t" and z[i+1] == "w" and z[i+2] == "o":
            if i < len(z)-4 and z[i+3] == "n" and z[i+4] == "e":
                ans.append(i+3)
                i+=5
            else:
                ans.append(i+2)
                i+=3
        elif z[i] == "o" and z[i+1] == "n" and z[i+2] == "e":
            ans.append(i+2)
            i += 3
        else:
            i+=1
    print(len(ans))
    print(*ans)

