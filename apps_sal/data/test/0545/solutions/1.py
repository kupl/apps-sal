#In the name of Allah

from sys import stdin, stdout
input = stdin.readline

n, t = list(map(int, input().split()))
s1 = input()[:-1]
s2 = list(input()[:-1])
if t > n:
        stdout.write("-1")
        return

d = [False] * n
m = 0
for i in range(n):
       if s2[i] == s1[i]:
               d[i] = True
               m += 1
d1 = d2 = n - t
ans = [""] * n

for i in range(n):
        if d[i] and d2 != 0 and d1 != 0:
                d2 -= 1
                d1 -= 1
                ans[i] = s1[i]
                #t -= 1

for i in range(n):
        if not d[i]:
                if d1 != 0:
                        ans[i] = s1[i]
                        d1 -= 1
                        continue
                if d2 != 0:
                        ans[i] = s2[i]
                        d2 -= 1
                        continue

for j in range(n):
        if ans[j] == "":
                for i in range(26):
                        al = chr(ord("a") + i)
                        if s1[j] != al and s2[j] != al:
                                ans[j] = al
                                break
                if ans[j] == "":
                        stdout.write("-1")

                
if d1 == 0 and d2 == 0:
        stdout.write("".join(ans))
else:
        stdout.write("-1")

