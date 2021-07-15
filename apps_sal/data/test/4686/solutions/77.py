w = input()
cnt = [0] * 26
for c in w:
    n = ord(c) - ord('a')
    cnt[n] += 1
for temp in cnt:
    if temp % 2 != 0:
        print("No")
        return
else:
    print("Yes")
