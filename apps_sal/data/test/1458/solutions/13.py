n = int(input())
s = input()
for i in range(1, n):
    if s[i] < s[i - 1]:
        print("YES")
        print(i, i + 1)
        break
else:
    print("NO")
