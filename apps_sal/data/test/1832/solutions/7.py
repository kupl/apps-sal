from sys import stdin
'\nn=int(stdin.readline().strip())\nn,m=map(int,stdin.readline().strip().split())\ns=list(map(int,stdin.readline().strip().split()))\n'
T = int(stdin.readline().strip())
let = [chr(i) for i in range(97, 97 + 26)]
for caso in range(T):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    ans = ['a' * 110]
    for i in range(n):
        x = ans[-1][0:s[i]]
        for j in let:
            if j != ans[-1][s[i]]:
                x += j
                break
        x += ans[-1][s[i] + 1:]
        ans.append(x)
    for i in ans:
        print(i)
