# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import collections
import math


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)
    j = 0    # Index of str1
    i = 0    # Index of str2
    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1
    return j == m


T = int(input())

#A,H,Q = [int(x) for x in stdin.readline().split()]
for t in range(T):
    #N,M = [int(x) for x in stdin.readline().split()]
    s = input()
    t = input()
    p = input()

    freq_s = {}
    freq_t = {}
    freq_p = {}
    for i in range(26):
        freq_s[chr(97 + i)] = 0
        freq_t[chr(97 + i)] = 0
        freq_p[chr(97 + i)] = 0

    for letter in s:
        freq_s[letter] += 1
    for letter in t:
        freq_t[letter] += 1
    for letter in p:
        freq_p[letter] += 1

    # check s is subsequence of t, if not, print no
    sub = isSubSequence(s, t)
    if sub == 0:
        print('NO')
    else:
        flag = 0
        for i in range(26):
            d = freq_t[chr(97 + i)] - freq_s[chr(97 + i)]
            if d > 0:
                # print(chr(97+i))
                if freq_p[chr(97 + i)] < d and flag == 0:
                    print('NO')
                    flag = 1

        if flag == 0:
            print('YES')
