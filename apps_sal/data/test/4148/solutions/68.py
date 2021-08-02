import string
N = int(input())
S = input()
ascii_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for s in S:
    s_index = ascii_uppercase.index(s)
    ans_index = (s_index + N) % len(ascii_uppercase)
    print(ascii_uppercase[ans_index], end="")
