import sys
import math
input = sys.stdin.readline


def inp():
    return(int(input()))


def inara():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))


s = insr()
ara = ["Sunny", "Cloudy", "Rainy", "Sunny", "Cloudy", "Rainy"]

if s[0] == 'S':
    print((ara[1]))
elif s[0] == 'C':
    print((ara[2]))
else:
    print((ara[0]))
