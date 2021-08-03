a = int(input())

dic = {}
dic[a] = 1

i = 1
while True:
    i += 1
    if a % 2 == 0:
        a //= 2
    else:
        a = 3 * a + 1

    if a in dic:
        break
    dic[a] = 1

print(i)
