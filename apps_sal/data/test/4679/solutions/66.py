code_A = ord('A')
code_a = ord('a')
A = [input() for _ in range(3)]

nxt = A[0][0]
A[0] = A[0][1:]
while True:
    now = ord(nxt) - code_a
    if A[now] == '':
        ans = chr(now + code_A)
        break
    nxt = A[now][0]
    A[now] = A[now][1:]

print(ans)
