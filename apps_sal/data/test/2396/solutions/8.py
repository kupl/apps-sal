from fractions import gcd

ans = []
dic = {}

n = int(input())
for i in range(n):
    word = input()
    word = word.replace('(', ',')
    word = word.replace('+', ',')
    word = word.replace(')/', ',')
    w = word.split(',')
    a = int(w[1])
    b = int(w[2])
    numerator = a + b
    denumerator = int(w[3])
    x = numerator // gcd(numerator, denumerator)
    y = denumerator // gcd(numerator, denumerator)
    ans.append((x, y))
    if (x, y) in dic:
        dic[(x, y)] += 1
    else:
        dic[(x, y)] = 1
for i in range(n):
    if i > 0:
        print(' ', end='')
    print(dic[ans[i]], end='')
print("\n", end='')
