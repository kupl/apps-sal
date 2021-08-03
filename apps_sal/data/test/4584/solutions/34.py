n = int(input())
a = list(map(int, input().split()))
c = [0] * n
for i in a:
    c[i - 1] += 1
for i in c:
    print(i)
