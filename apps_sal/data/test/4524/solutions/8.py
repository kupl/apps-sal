n, m = list(map(int, input().split()))
a = input()
b = input()
n, m = len(a), len(b)
if n > m:
    addition = ''.join(["0"] * (n - m))
    b = addition + b
elif m > n:
    addition = ''.join(["0"] * (m - n))
    a = addition + a

#print(a)
#print(b)

l = max(m, n)
count_bigger = [0] * l
acc = 0
for i in range(l):
    if b[i] == "1":
        acc += 1
    if a[i] == "1":
        count_bigger[i] = acc

count_bigger = count_bigger[::-1]
answer = 0
mul = 1
for i in range(l):
    if count_bigger[i] != 0:
        answer += count_bigger[i] * mul
    mul *= 2
    mul %= 998244353

answer %= 998244353
print(answer)
