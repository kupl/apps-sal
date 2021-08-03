n = int(input())
w = [input()]
for i in range(n - 1):
    s = input()
    if s in w or w[i][-1] != s[0]:
        print("No")
        return
    w.append(s)
print("Yes")
