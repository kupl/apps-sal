n = int(input())
letter = str(input())
if '1' not in letter:
    print(0)
    quit()
if '1 1' not in letter:
    print(2 * letter.count('1') - 1)
    quit()
op = 2 * letter.count('1') - 1
for i in range(n - 1):
    if letter[2 * i] == '1' and letter[2 * i + 2] == '1':
        op -= 1
print(op)
