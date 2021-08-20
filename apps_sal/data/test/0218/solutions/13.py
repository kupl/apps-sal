import sys
if False:
    inp = open('A.txt', 'r')
else:
    inp = sys.stdin
(n, p, q) = list(map(int, inp.readline().split()))
string = inp.readline().strip()
length = n
ans = -1
for i in range(n // p + 1):
    length = n - p * i
    if length % q == 0:
        ans = i
        break
if ans == -1:
    print(-1)
else:
    print(ans + length // q)
    for i in range(ans):
        print(string[:p])
        string = string[p:]
    for i in range(length // q):
        print(string[:q])
        string = string[q:]
