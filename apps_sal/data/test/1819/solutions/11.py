from sys import stdin, stdout
import math

T = int(input())

for i in range(T):
    N, X = [int(x) for x in stdin.readline().split()]

    print(X * 2)
