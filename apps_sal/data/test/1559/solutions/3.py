import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
    return list(map(int, sys.stdin.readline().split()))


def num():
    return map(int, sys.stdin.readline().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return x * y // gg


def findSum(str1, str2):
    if len(str1) > len(str2):
        t = str1
        str1 = str2
        str2 = t
    str = ''
    n1 = len(str1)
    n2 = len(str2)
    str1 = str1[::-1]
    str2 = str2[::-1]
    carry = 0
    for i in range(n1):
        sum = ord(str1[i]) - 48 + (ord(str2[i]) - 48 + carry)
        str += chr(sum % 10 + 48)
        carry = int(sum / 10)
    for i in range(n1, n2):
        sum = ord(str2[i]) - 48 + carry
        str += chr(sum % 10 + 48)
        carry = int(sum / 10)
    if carry:
        str += chr(carry + 48)
    str = str[::-1]
    return str


mm = 1000000007


def solve():
    t = 1
    for tt in range(t):
        n = nu()
        s = input()
        if len(s) % n != 0:
            nm = len(s) // n + 1
            hp = '1'
            for i in range(n - 1):
                hp += '0'
            op = ''
            for i in range(nm):
                op += hp
            print(op)
            continue
        ff = s[0:n]
        ox = s[n:]
        vv = ''
        for i in range(len(s)):
            vv += '9'
        if vv == s:
            nm = len(s) // n + 1
            hp = '1'
            for i in range(n - 1):
                hp += '0'
            op = ''
            for i in range(nm):
                op += hp
            print(op)
            continue
        gp = ''
        last = -1
        ok = -1
        for i in range(0, len(ox), n):
            for j in range(i, i + n):
                if ff[j - i] < ox[j]:
                    last = 1
                    break
                if ff[j - i] > ox[j]:
                    ok = j + 1
                    break
            if last != -1:
                break
            if ok != -1:
                break
        ans = ''
        if last != -1:
            gp = findSum(ff, '1')
            for i in range(len(s) // n):
                print(gp, end='')
            continue
        if ok != -1:
            for i in range(len(s) // n):
                print(ff, end='')
            continue
        gp = findSum(ff, '1')
        for i in range(len(s) // n):
            print(gp, end='')


def __starting_point():
    solve()


__starting_point()
