n = int(input())
s = [int(input()) for i in range(n)]
if sum(s) % 10 != 0:
    print(sum(s))
else:
    s.sort()
    flag = 0
    for i in range(n):
        if s[i] % 10 != 0:
            print(sum(s) - s[i])
            flag = 1
            break
    if flag == 0:
        print(0)
