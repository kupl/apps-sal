N = int(input())
S = input()
code_A = ord('A')
results = ''
for c in S:
    after_n = (ord(c) + N - code_A) % 26
    results += chr(code_A + after_n)
print(results)
