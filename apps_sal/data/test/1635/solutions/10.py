n = int(input())
A = list(map(int, input().split()))
c = dict()
for i in range(n):
    a = A[i]
    c[a] = i
mini = 100000000000000
numb = 0
for i in c:
    if c[i] < mini:
        numb = i
        mini = c[i]
print(numb)
