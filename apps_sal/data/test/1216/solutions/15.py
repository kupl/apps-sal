a = int(input())
s = input()
ans = ""

i = 0
while i <= (a - 1):
    if (s[i] == "a") or (s[i] == "i") or (s[i] == "u") or (s[i] == "y"):
        j = i
        while(j < (a - 1)) and (s[j] == s[j + 1]):
            j += 1
        print(s[i], end="")
        i = j + 1

    elif (s[i] == "o") or (s[i] == "e"):
        j = i
        while(j < a - 1) and (s[j] == s[j + 1]):
            j += 1
        k = 1
        if(j - i) == 1:
            k = 2
        print(s[i] * k, end="")
        i = j + 1

    else:
        print(s[i], end="")
        i += 1
