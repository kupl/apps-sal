t = int(input())
for i in range(t):
    k = 0
    n = input()
    k += (len(n) - 1) * 9
    if n[0] * len(n) > n:
        k += int(n[0]) - 1
    else:
        k += int(n[0])
    print(k)
