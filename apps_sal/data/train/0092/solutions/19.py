q = int(input())
for i in range(q):
    s1 = input()
    s2 = input()
    f = 1
    for i in range(len(s1)):
        for j in range(len(s2)):
            if f and s1[i] == s2[j]:
                print("YES")
                f = 0
    if f:
        print("NO")

