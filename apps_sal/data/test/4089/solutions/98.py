N = int(input())
ans_reverse = ''


def num_to_alphabet(n):
    return chr(ord('a') - 1 + n)


while N:
    if N % 26 == 0:
        ans_reverse += 'z'
        N -= 26
    else:
        ans_reverse += num_to_alphabet(N % 26)
    N //= 26
print(ans_reverse[::-1])
