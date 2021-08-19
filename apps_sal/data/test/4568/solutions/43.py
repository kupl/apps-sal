n = int(input())
s = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
max_chr = 0
for i in range(len(s) - 1):
    cnt = 0
    for letter in alphabets:
        if letter in s[:i + 1] and letter in s[i + 1:]:
            cnt += 1
    max_chr = max(max_chr, cnt)
print(max_chr)
