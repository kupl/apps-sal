n = input()
n = n.replace('7', '1')
n = n.replace('4', '0')
length = len(n)
answer = 0
for i in range(length):
    answer += 2 ** i
t = 1
for d in reversed(n):
    if d == '1':
        answer += t
    t *= 2
print(answer)
