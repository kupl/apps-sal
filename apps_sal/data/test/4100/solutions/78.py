import math
import collections
import itertools


def resolve():

    N, K, Q = list(map(int, input().split()))
    A = [0] * Q
    Aans = [0] * N

    for i in range(Q):
        A[i] = int(input())
        Aans[A[i] - 1] += 1

    for i in range(N):
        if(0 >= K - Q + (Aans[i])):
            print("No")
        else:
            print("Yes")


resolve()
