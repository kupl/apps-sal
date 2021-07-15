n = int(input())
s = []
for i in range(n):
    k = input()
    s.append(k)
maxans = -1
for i in range(26):
    for j in range(26):
        ans = 0
        for k in s:
            for p in range(len(k)):
                if k[p] != chr(ord('a') + i) and k[p] != chr(ord('a') + j):
                    break
            if k[p] == chr(ord('a') + i) or k[p] == chr(ord('a') + j):
                ans += len(k)
        if ans > maxans:
            maxans = ans
print(maxans)

