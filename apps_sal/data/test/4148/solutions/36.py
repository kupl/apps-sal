N = int(input())
S = input()
answer = []
for s in S:
    answer.append(chr(((ord(s) + N - 65) % 26) + 65))
print(''.join(answer))
