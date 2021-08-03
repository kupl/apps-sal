s = input()
k = int(input())
cnt = 0
for j in range(len(s)):
    cnt += 1
    if s[j] == "1":
        if cnt == k:
            print("1")
            return
    else:
        print((s[j]))
        return
