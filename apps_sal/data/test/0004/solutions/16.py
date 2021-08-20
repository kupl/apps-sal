from sys import stdin, stdout
x = int(stdin.readline())
(a, b) = list(map(int, stdin.readline().split()))
time = a * 60 + b
for i in range(10 ** 6):
    t = time - i * x
    if t < 0:
        t += 24 * 60
        time += 24 * 60
    if '7' in str(t // 60) + str(t % 60):
        stdout.write(str(i))
        break
