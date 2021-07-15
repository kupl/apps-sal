s = input()

n, m = list(map(int, s.split(' ')))

l = [0]

for i in range(n):
    s = input()
    t1, t2 = list(map(int, s.split(' ')))
    l.append(l[-1] + t1*t2)

xs = list(map(int, input().split(' ')))

j = 0
i = 0
while i < m:
    if xs[i] <= l[j]:
        print(j)
        i += 1
    else:
        j += 1

