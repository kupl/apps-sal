n = int(input())
s = input()

f1 = 0
while True:
    f = s.find("ogo")
    if f > -1:
        f1 = f+3
        while True:
            if f1 + 2 <= n:
                if s[f1:f1+2] == "go":
                    f1 += 2
                else:
                    break
            else:
                break
        s = s[:f] + "***" + s[f1:]
    else:
        break
print(s)
                

