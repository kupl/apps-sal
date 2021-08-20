d = {}
non_zeroes = []
letters = list('abcdefghij')
for letter in letters:
    d[letter] = 0
n = int(input())
for i in range(n):
    s = input()
    j = 1
    for letter in s:
        if j == 1 and letter not in non_zeroes:
            non_zeroes.append(letter)
        d[letter] += 10 ** (len(s) - j)
        j += 1
max = 0
zero = ''
for letter in d.keys():
    if d[letter] > max and letter not in non_zeroes:
        zero = letter
        max = d[letter]
if zero in d.keys():
    d.pop(zero)
sum = 0
num = 1
for item in sorted(d.items(), key=lambda x: -x[1]):
    sum += num * item[1]
    num += 1
print(sum)
