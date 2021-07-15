def f(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    a = [0] * 26
    b = [0] * 26
    for i in range(n1):
        a[ord(s1[i]) - ord('a')] += 1

    for i in range(n2):
        b[ord(s2[i]) - ord('a')] += 1
        if i >= n1:
            b[ord(s2[i - n1]) - ord('a')] -= 1
        if a == b:
            print("YES")
            return
    print("NO")

n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    f(s1, s2)

