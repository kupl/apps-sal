T = int(input())
for i in range(0, T):
    s, i, exp = (int(i) for i in input().split())
    if (s + exp <= i):
        print(0)
    elif (i + exp < s):
        print(exp + 1)
    else:
        print(exp + 1 - (i + exp - s + 2) // 2)
