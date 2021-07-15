k = int(input())
for da in range(k):
    n = int(input())
    s1 = input()
    s2 = input()
    a = []
    for i in range(n):
        if s1[i] != s2[i]:
            a.append(i)
    if len(a) == 0:
        print("Yes")
        continue
    if len(a) != 2:
        print("No")
        continue
    if s1[a[0]]==s1[a[1]] and s2[a[0]]==s2[a[1]]:
        print("Yes")
    else:
        print("No")

