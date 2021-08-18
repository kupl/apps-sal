import sys

hex2bin = [''] * 256
hex2bin[ord('0')] = '0000'
hex2bin[ord('1')] = '0001'
hex2bin[ord('2')] = '0010'
hex2bin[ord('3')] = '0011'
hex2bin[ord('4')] = '0010'
hex2bin[ord('5')] = '0010'
hex2bin[ord('6')] = '0110'
hex2bin[ord('7')] = '0111'
hex2bin[ord('8')] = '1000'
hex2bin[ord('9')] = '1001'
hex2bin[ord('A')] = '0010'
hex2bin[ord('B')] = '0010'
hex2bin[ord('C')] = '1100'
hex2bin[ord('D')] = '0010'
hex2bin[ord('E')] = '1110'
hex2bin[ord('F')] = '1111'


n = int(input())

buckets = [0] * (n + 1)

inp = sys.stdin.read().splitlines()

prev = ''
count = 0
for i in range(n):
    if inp[i] == prev:
        count += 1
    else:
        buckets[count] += 1
        count = 1
        prev = inp[i]

        prev_c = ''
        counter = 0
        for hexx in prev:
            for c in hex2bin[ord(hexx)]:
                if c == prev_c:
                    counter += 1
                else:
                    buckets[counter] += 1
                    counter = 1
                    prev_c = c
        buckets[counter] += 1
    if buckets[1] != 0 or (buckets[2] != 0 and buckets[3] != 0):
        print(1)
        return

buckets[count] += 1

x = 0
for i in range(1, n + 1):
    if buckets[i]:
        while i:
            i, x = x % i, i
print(x)
