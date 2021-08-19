#!/usr/bin/env python3
"""Compute z function."""


def compute_z(data):
    z = [0 for _ in range(len(data))]
    z[0] = len(data)
    l = 0
    r = 0
    for i in range(1, len(data)):
        if i <= r:  # nu am explorat
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < len(data) and data[z[i]] == data[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            r = i + z[i] - 1
            l = i
    return z


data = input()  # input -> eval 2.x ; input = read
# print(data)
n = len(data)
z = compute_z(data)
feq_z = [0 for _ in range(n)]  # range(3) = 0, 1, 2
for value in z:
    if value == 0:
        continue
    index = value - 1
    feq_z[index] += 1


for i in range(n - 2, -1, -1):
    feq_z[i] += feq_z[i + 1]

# print(z)
# print(feq_z)
count = 0
for i in range(n - 1, -1, -1):
    if z[i] == n - i:
        count += 1
print(count)
for i in range(n - 1, -1, -1):
    if z[i] == n - i:
        print("{} {}".format(z[i], feq_z[z[i] - 1]))
