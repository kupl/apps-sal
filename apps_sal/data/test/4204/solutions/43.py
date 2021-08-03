s = input()
k = int(input())

if k == 1:
    print(int(s[0]))
elif s[0] == "1":
    cnt = 0
    while cnt < len(s) and s[cnt] == "1":
        cnt += 1
    if cnt >= k:
        print(1)
    elif cnt == len(s):
        print("1")
    else:
        print(s[cnt])
else:
    print(int(s[0]))
