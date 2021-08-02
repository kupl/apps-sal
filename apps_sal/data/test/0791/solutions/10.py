n = int(input())
s = input()
swaps = 0
k = 0
for i in range(len(s)):
    if int(s[i]) == 0:
        k += 1
        break
    k += 1
print(k)
