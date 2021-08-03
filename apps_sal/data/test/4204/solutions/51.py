s = input()
k = int(input())

if k == 1:
    print(s[0])
else:
    for i in range(len(s)):
        if s[i] != "1":
            print(s[i])
            break
        elif i + 1 == k:
            print(s[i])
            break
