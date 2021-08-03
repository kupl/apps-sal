for i in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    count = 0
    s1 = []
    t1 = []
    for j in range(n):
        if s[j] != t[j]:
            count += 1
            s1.append(s[j])
            t1.append(t[j])
    if count == 2 and s1[0] == s1[1] and t1[0] == t1[1]:
        print("Yes")
    else:
        print("No")
