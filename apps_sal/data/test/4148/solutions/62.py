N = int(input())
S = input()
answer = ''
for x in S:
    x = chr(ord(x) + N)
    if ord(x) > ord('Z'):
        x = chr(ord('A') + (ord(x) - ord('Z') - 1))
    answer += x
print(answer)
