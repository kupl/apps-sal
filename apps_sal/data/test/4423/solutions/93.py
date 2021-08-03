n = int(input())
rest = [list([*input().split(), i + 1]) for i in range(n)]
rest = list(sorted(rest, key=lambda x: (x[0], 100 - int(x[1]))))
for i in rest:
    print(i[2])
