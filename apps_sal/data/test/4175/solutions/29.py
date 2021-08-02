n = int(input())
w = str(input())
a = []
a.append(w)
for i in range(1, n):
    x = w[len(w) - 1]
    w = str(input())
    if x != w[0] or w in a:
        print("No")
        return
    a.append(w)

print("Yes")
