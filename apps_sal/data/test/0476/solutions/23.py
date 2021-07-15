v = input()
i = 0
while i <= len(v) - 1:
    if v[0] != "1":
        print("NO")
        break
    if v[i] == "1":
        if i + 1 <= len(v) - 1:
            if v[i + 1] == "4":
                if i + 2 <= len(v) - 1:
                    if v[i + 2] == "4":
                        i += 2
                    else:
                        i += 1
                else:
                    print('YES')
                    break
    else:
        print("NO")
        break
    i += 1
else:
    print('YES')



