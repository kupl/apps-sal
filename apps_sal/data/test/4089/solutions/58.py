N = int(input())
S = ''
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while N > 0:
    if N % 26 != 0:
        S = alphabets[N % 26 - 1] + S
        N = (N - N % 26) // 26
    else:
        S = alphabets[N % 26 - 1] + S
        N = (N - 26) // 26
print(S)
