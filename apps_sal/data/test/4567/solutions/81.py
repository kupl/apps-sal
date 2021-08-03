n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort()

m = -1
for i in s:
    if i % 10 != 0:
        m = i
        break

if sum(s) % 10 == 0:
    if m == -1:
        print(0)
    else:
        print(sum(s) - m)
else:
    print(sum(s))
