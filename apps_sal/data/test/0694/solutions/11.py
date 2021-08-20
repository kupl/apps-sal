s = input()
(a, b) = map(int, input().split())
tens = 1
B = 0
A = 0
posa = [False] * (len(s) + 1)
posb = [False] * (len(s) + 1)
tens = 1
for i in range(len(s) - 1, -1, -1):
    B += int(s[i]) * tens % b
    B = B % b
    if B == 0:
        posb[i] = True
    tens = tens * 10 % b
loda = True
for i in range(len(s) - 1):
    A = A * (10 % a) % a
    A += int(s[i]) % a
    A = A % a
    if A == 0:
        posa[i] = True
for i in range(len(s)):
    if posa[i] == True and posb[i + 1] == True and (s[i + 1] != '0'):
        loda = False
        print('YES')
        print(s[:i + 1])
        print(s[i + 1:])
        break
if loda:
    print('NO')
