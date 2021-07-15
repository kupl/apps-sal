s = input()
n = int(input())
D = {}
if n <= len(s):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        D[i] = 0
    for i in s:
        D[i] += 1
    ans = 0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if D[i] != 0:
            ans += 1
    if n >= ans:
        print(n - ans)
    else:
        print(0)
else:
    print('impossible')



