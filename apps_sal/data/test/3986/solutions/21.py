n, k = [int(x) for x in input().split()]

if k > n or k == 1 and n > 1:
    print(-1)
elif k == 1 and n == 1:
    print('a')
else:
    first_char = 97
    letters = [chr(x) for x in range(first_char, first_char+k)]

    word = ('ab' * (n+1 // 1))[:n-k+2]
    word += ''.join(letters[2:k])

    print(word)

