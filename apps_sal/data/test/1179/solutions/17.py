from sys import stdin, stdout
(n, k) = map(int, stdin.readline().split())
number = [0]
for i in range(n):
    number.append(number[-1] + i + 1)
    if number[-1] >= k:
        ind = i
        cnt = number[-2]
        break
values = list(map(int, stdin.readline().split()))
for i in range(ind + 1):
    if cnt + i + 1 == k:
        stdout.write(str(values[i]))
        break
