# coding: utf-8
# Your code here!

a = int(input())
b = int(input())
c = int(input())
x = int(input())

max_a = min(int(x / 500), a)
max_b = min(int(x / 100), b)
max_c = min(int(x / 50), c)

cnt = 0

for i in range(max_a + 1):
    for j in range(max_b + 1):
        for k in range(max_c + 1):
            if i * 500 + j * 100 + k * 50 == x:
                cnt += 1

print(cnt)
