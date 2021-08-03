n, num = int(input()), list(map(int, input().split()))
sort = list(sorted(num))
for i in range(n - 1):
    num[i + 1] += num[i]
    sort[i + 1] += sort[i]
num, sort = [0] + num, [0] + sort
for i in range(int(input())):
    t, l, r = list(map(int, input().split()))
    print(num[r] - num[l - 1] if t == 1 else sort[r] - sort[l - 1])
