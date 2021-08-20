n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
cr = list(map(int, input().split(' ')))
val = []
for i in range(n):
    val.append(sum(a[0:i]) + cr[i] + sum(b[i:]))
val.sort()
print(val[0] + val[1])
