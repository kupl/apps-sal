input()
l = list(input())
x = list(map(int, input().split(' ')))

p = [i for i in range(len(l) - 1) if l[i] == 'R' and l[i + 1] == 'L']

if not p:
    print(-1)
else:
    t = [x[i + 1] - x[i] for i in p]
    print(min(t) // 2)
