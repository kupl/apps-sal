N = int(input())
A = list(map(int, input().split()))
a = 0
s = []
for i in A:
    if i < a:
        s.append(a - i)
    else:
        a = i
print(sum(s))
