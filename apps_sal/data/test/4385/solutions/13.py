import sys
import math

a = [int(input()) for i in range(5)]
k = int(input())
for i in range(5):
    for j in range(5):
        if (a[i] - a[j]) > k:
            print(":(")
            return
print("Yay!")
