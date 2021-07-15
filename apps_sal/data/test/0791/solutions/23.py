n = int(input())
bits = input()
x = int(bits[::-1], 2)
x += 1
if x == 2 ** n:
    x = 0
t = bin(x)[2:]
bits2 = ('0' * (n - len(t)) + t)[::-1]
cnt = 0
for i in range(n):
    if bits[i] != bits2[i]:
        cnt += 1
print(cnt)
