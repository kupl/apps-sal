import sys
(t, a) = input().split('.')
(t, b) = input().split('.')
(t, c) = input().split('.')
(t, d) = input().split('.')
k = [0] * 4
if 2 * len(a) <= len(b) and 2 * len(a) <= len(c) and (2 * len(a) <= len(d)):
    k[0] = 1
if 2 * len(b) <= len(a) and 2 * len(b) <= len(c) and (2 * len(b) <= len(d)):
    k[1] = 1
if 2 * len(c) <= len(a) and 2 * len(c) <= len(b) and (2 * len(c) <= len(d)):
    k[2] = 1
if 2 * len(d) <= len(a) and 2 * len(d) <= len(b) and (2 * len(d) <= len(c)):
    k[3] = 1
s = [0] * 4
if 2 * len(b) <= len(a) and 2 * len(c) <= len(a) and (2 * len(d) <= len(a)):
    s[0] = 1
if 2 * len(a) <= len(b) and 2 * len(c) <= len(b) and (2 * len(d) <= len(b)):
    s[1] = 1
if 2 * len(a) <= len(c) and 2 * len(b) <= len(c) and (2 * len(d) <= len(c)):
    s[2] = 1
if 2 * len(a) <= len(d) and 2 * len(b) <= len(d) and (2 * len(c) <= len(d)):
    s[3] = 1
if sum(k) + sum(s) == 1:
    if k[0] == 1:
        print('A')
    if k[1] == 1:
        print('B')
    if k[2] == 1:
        print('C')
    if k[3] == 1:
        print('D')
    if s[0] == 1:
        print('A')
    if s[1] == 1:
        print('B')
    if s[2] == 1:
        print('C')
    if s[3] == 1:
        print('D')
else:
    print('C')
