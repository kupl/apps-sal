n = int(input())
s = input()
l = list(map(int, input().split()))
L = [0 for i in range(n)]
i = 0
while (True):
    if L[i] == -1:
        print("INFINITE")
        return
    L[i] = -1
    if s[i] == ">":
        i += l[i]
    else:
        i -= l[i]
    if i <= -1 or i >= n:
        print("FINITE")
        return
