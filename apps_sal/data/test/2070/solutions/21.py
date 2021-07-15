__author__ = 'Andrey'


def val(char):
    nonlocal values
    return values[ord(char) - ord("a")]


values = list(map(int, input().split()))
s = input()
prefix_sums = [val(s[0])]
for q in range(1, len(s)):
    prefix_sums.append(prefix_sums[q - 1] + val(s[q]))
big_dict = dict()
for i in range(97, 97 + 26):
    big_dict[chr(i)] = dict()
ans = 0
for index in range(len(s)):
    letter = s[index]
    if index > 0:
        ans += big_dict[letter].get(prefix_sums[index - 1], 0)
    big_dict[letter][prefix_sums[index]] = big_dict[letter].get(prefix_sums[index], 0) + 1
print(ans)
