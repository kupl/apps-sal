N = int(input())
mas = [False] * 90
li = list(map(int, input().split()))
for i in li:
    mas[i - 1] = True
i = 0
sk = 0
while (sk < 15) and (i < 90):
    if (not mas[i]):
        sk += 1
    else:
        sk = 0
    i += 1
print(i)
