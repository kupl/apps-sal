from string import ascii_lowercase

N = int(input())

d = ""
while N > 0:
    N -= 1
    c = N % 26
    N = N // 26
    d = d + ascii_lowercase[c]

print(d[::-1])
