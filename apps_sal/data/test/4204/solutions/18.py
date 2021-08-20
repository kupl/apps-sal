s = input()
k = int(input())
for i in range(len(s)):
    n = int(s[i])
    if i + 1 == k:
        print(n)
        break
    elif n != 1:
        print(n)
        break
