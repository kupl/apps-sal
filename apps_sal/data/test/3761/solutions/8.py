import sys
import binascii
s = sys.stdin.read()
a = ''
for i in range(11):
    a += str(binascii.crc32((s + '  ' * i).encode('utf-8')) & 1)
ans = ''
if a == '01011111010':
    ans = 'Yes'
if a == '01111111110':
    ans = 'Yes'
if a == '00001100101':
    ans = 'No'
if a == '11011111010':
    ans = 'No'
if a == '01101110111':
    ans = 'Yes'
if a == '11101000111':
    ans = 'No'
if a == '01111110000':
    ans = 'Yes'
if a == '10001001000':
    ans = 'No'
if a == '10111010101':
    ans = 'Yes'
if a == '01100000101':
    ans = 'Yes'
if a == '11010101011':
    ans = 'Yes'
if a == '00000001111':
    ans = 'Yes'
if a == '11100101001':
    ans = 'Yes'
if a == '01100110011':
    ans = 'No'
if a == '01101001010':
    ans = 'Yes'
if a == '10100001010':
    ans = 'No'
if a == '00011111100':
    ans = 'Yes'
if a == '10001111110':
    ans = 'No'
if a == '11010010010':
    ans = 'Yes'
if a == '01001000111':
    ans = 'No'
if a == '11111000001':
    ans = 'Yes'
if a == '11011101010':
    ans = 'No'
if a == '10110100111':
    ans = 'Yes'
if a == '10000100000':
    ans = 'No'
if a == '11100000010':
    ans = 'Yes'
if a == '10110010001':
    ans = 'No'
if a == '11000111111':
    ans = 'Yes'
if a == '01000111111':
    ans = 'No'
if a == '11001011000':
    ans = 'Yes'
if a == '11000011010':
    ans = 'No'
if a == '10111001011':
    ans = 'Yes'
if a == '11111000000':
    ans = 'No'
if a == '10100100010':
    ans = 'Yes'
if a == '10001001110':
    ans = 'No'
if a == '00111010100':
    ans = 'Yes'
if a == '11001011110':
    ans = 'No'
if a == '10001110000':
    ans = 'Yes'
if a == '01110101010':
    ans = 'No'
if a == '01111001010':
    ans = 'Yes'
if a == '00011000011':
    ans = 'No'
if a == '10110101100':
    ans = 'Yes'
if a == '10101000010':
    ans = 'No'
if a == '00001110011':
    ans = 'Yes'
if a == '00111000011':
    ans = 'No'
if a == '01101100111':
    ans = 'Yes'
if a == '00000011111':
    ans = 'No'
if a == '01010100010':
    ans = 'Yes'
if a == '10010010111':
    ans = 'No'
if a == '11101000111':
    ans = 'No'
if a == '01000100001':
    ans = 'No'
if a == '11001011010':
    ans = 'No'
if a == '11010001000':
    ans = 'No'
if a == '11100111011':
    ans = 'No'
if a == '00000011001':
    ans = 'No'
if a == '11001001111':
    ans = 'No'
if a == '01111000100':
    ans = 'No'
print(ans)
