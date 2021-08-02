a = int(input())
b = list(map(int, input().split()))
c = [0]
for i in b:
    c.append(i + c[-1])
for i in range(int(input())):
    l, r = map(int, input().split())
    print((c[r] - c[l - 1]) // 10)
