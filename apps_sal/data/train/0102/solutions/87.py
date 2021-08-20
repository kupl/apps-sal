t = int(input())
for i in range(t):
    n = input()
    res = (len(n) - 1) * 9
    res += int(n) // int(n[0] * len(n))
    res += int(n[0]) - 1
    print(res)
