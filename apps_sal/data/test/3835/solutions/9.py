n = int(input())
m = list(map(int, input().split()))[1:]
a = list(map(int, input().split()))[2]
for i in range(n - 2):
    input()
b = int((m[0] * m[1] / a) ** 0.5)
print(b, end=' ')
for el in m:
    print(el // b, end=' ')
